#!/usr/bin/env python3
"""
Apply quality scores to skills database based on:
1. Manual assessments from quality_scores_collected.json
2. Derived scoring model based on observed patterns
"""

import sqlite3
import json
import re
from pathlib import Path

DB_PATH = Path(__file__).parent / "skills.db"
SCORES_PATH = Path(__file__).parent / "quality_scores_collected.json"

def load_manual_scores():
    """Load manually assessed scores."""
    with open(SCORES_PATH) as f:
        data = json.load(f)
    
    scores = {}
    for registry, skills in data.items():
        if registry.startswith("_"):
            continue
        for skill in skills:
            key = (skill["name"], registry.replace("_partial", ""))
            scores[key] = (skill["score"], skill["rationale"])
    return scores

def score_skill_content(skill_md: str, description: str) -> tuple[int, str]:
    """
    Score a skill based on content analysis.
    Returns (score, rationale) based on patterns observed in high-quality skills.
    """
    if not skill_md:
        return 30, "No skill content available"
    
    content = skill_md.lower()
    score = 50  # Base score
    factors = []
    
    # Positive signals (observed in 90+ scored skills)
    
    # 1. Structured workflow (+15 max)
    workflow_patterns = [
        r'#+\s*(workflow|process|steps|phases?)',
        r'(step\s*\d|phase\s*\d|\d\.\s*\*\*)',
        r'decision\s*tree',
        r'flowchart|mermaid',
    ]
    workflow_score = sum(3 for p in workflow_patterns if re.search(p, content))
    if workflow_score > 0:
        factors.append(f"workflow structure +{min(workflow_score, 15)}")
    score += min(workflow_score, 15)
    
    # 2. Code examples (+12 max)
    code_blocks = len(re.findall(r'```\w+', content))
    if code_blocks >= 5:
        score += 12
        factors.append("extensive code examples +12")
    elif code_blocks >= 2:
        score += 8
        factors.append("code examples +8")
    elif code_blocks >= 1:
        score += 4
        factors.append("some code +4")
    
    # 3. Bundled scripts/assets (+10 max)
    script_patterns = [
        r'scripts?/',
        r'\.py\b',
        r'\.sh\b',
        r'\.js\b',
        r'bundled',
        r'bin/',
    ]
    script_score = sum(2 for p in script_patterns if re.search(p, content))
    if script_score > 0:
        factors.append(f"bundled scripts/assets +{min(script_score, 10)}")
    score += min(script_score, 10)
    
    # 4. Clear triggers/conditions (+8 max)
    trigger_patterns = [
        r'when\s+to\s+use',
        r'trigger|invoke|activate',
        r'use\s+this\s+(skill|when)',
        r'best\s+for',
    ]
    trigger_score = sum(2 for p in trigger_patterns if re.search(p, content))
    if trigger_score > 0:
        factors.append(f"clear triggers +{min(trigger_score, 8)}")
    score += min(trigger_score, 8)
    
    # 5. Error handling/troubleshooting (+5)
    if re.search(r'error|troubleshoot|fallback|exception|fail', content):
        score += 5
        factors.append("error handling +5")
    
    # 6. Best practices/anti-patterns (+5)
    if re.search(r'best\s*practice|anti.?pattern|don\'t|avoid|never', content):
        score += 5
        factors.append("best practices +5")
    
    # 7. Reference documentation (+3)
    if re.search(r'reference|documentation|see\s+also|learn\s+more', content):
        score += 3
        factors.append("references +3")
    
    # Negative signals (observed in 50- scored skills)
    
    # 1. Template/placeholder content (-15)
    if re.search(r'placeholder|todo:|tbd|coming\s+soon|<.*>', content):
        score -= 15
        factors.append("placeholder content -15")
    
    # 2. Very short content (-10)
    if len(content) < 500:
        score -= 10
        factors.append("very short -10")
    elif len(content) < 1000:
        score -= 5
        factors.append("brief content -5")
    
    # 3. Generic/vague claims (-8)
    if re.search(r'world.?class|best\s+in|expert\s+level|pro\s*max', content):
        if not re.search(r'```', content):  # vague claims without code
            score -= 8
            factors.append("vague claims without substance -8")
    
    # 4. Heavy external dependencies (-5)
    if re.search(r'requires?\s+.{0,20}(mcp|external|api\s+key)', content):
        if not re.search(r'fallback|alternative', content):
            score -= 5
            factors.append("heavy external deps -5")
    
    # Clamp to valid range
    score = max(20, min(98, score))
    
    rationale = "; ".join(factors) if factors else "baseline content"
    return score, rationale

def update_database():
    """Update database with quality scores."""
    manual_scores = load_manual_scores()
    
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    # Ensure quality_score column exists with rationale
    try:
        cur.execute("ALTER TABLE skills ADD COLUMN quality_rationale TEXT")
    except sqlite3.OperationalError:
        pass  # Column already exists
    
    # Get all skills
    cur.execute("SELECT id, slug, name, registry, skill_md, description FROM skills")
    rows = cur.fetchall()
    
    updated = 0
    for row in rows:
        skill_id, slug, name, registry, skill_md, description = row
        
        # Check for manual score first
        key = (name, registry)
        if key in manual_scores:
            score, rationale = manual_scores[key]
            rationale = f"[manual] {rationale}"
        elif (slug, registry) in manual_scores:
            score, rationale = manual_scores[(slug, registry)]
            rationale = f"[manual] {rationale}"
        else:
            # Apply content-based scoring
            score, rationale = score_skill_content(skill_md or "", description or "")
            rationale = f"[derived] {rationale}"
        
        cur.execute(
            "UPDATE skills SET quality_score = ?, quality_rationale = ? WHERE id = ?",
            (score, rationale, skill_id)
        )
        updated += 1
    
    conn.commit()
    
    # Print summary statistics
    cur.execute("""
        SELECT registry, 
               COUNT(*) as count,
               ROUND(AVG(quality_score), 1) as avg_score,
               MIN(quality_score) as min_score,
               MAX(quality_score) as max_score
        FROM skills 
        GROUP BY registry
    """)
    
    print("Quality Score Summary by Registry:")
    print("-" * 60)
    for row in cur.fetchall():
        print(f"{row[0]:20} | count: {row[1]:4} | avg: {row[2]:5.1f} | range: {row[3]}-{row[4]}")
    
    # Top skills by score
    print("\n\nTop 20 Skills by Quality Score:")
    print("-" * 80)
    cur.execute("""
        SELECT name, registry, quality_score, quality_rationale
        FROM skills
        ORDER BY quality_score DESC
        LIMIT 20
    """)
    for row in cur.fetchall():
        print(f"{row[2]:3} | {row[0][:40]:40} | {row[1]:10}")
    
    conn.close()
    print(f"\nUpdated {updated} skills")

if __name__ == "__main__":
    update_database()
