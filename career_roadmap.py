from collections import namedtuple

# Define our Quest structure
Quest = namedtuple('Quest', ['id', 'task', 'status', 'xp_reward'])

def update_quest_log():
    # Active Quest Data
    quests = [
        Quest(1, "Complete Wwise 101 & 135", "IN PROGRESS", 500),
        Quest(2, "Post 30s Implementation Clip", "LOCKED", 250),
        Quest(3, "Record 5 Unique Office Sounds", "OPEN", 100),
        Quest(4, "C# Unity Audio Hooks Study", "OPEN", 400)
    ]

    print(f"\n{'ID':<3} | {'ACTIVE QUEST':<32} | {'STATUS':<12} | {'XP'}")
    print("-" * 65)
    
    for q in quests:
        status_icon = "⏳" if q.status == "IN PROGRESS" else "⭕"
        print(f"{q.id:<3} | {q.task:<32} | {status_icon} {q.status:<10} | {q.xp_reward}")

def main():
    print("\n" + "!"*20 + " SYSTEM CHECK: OKAY " + "!"*20)
    print("LOG: Modules 'collections' and 'math' initialized.")
    
    update_quest_log()
    
    # Using 'math' for a progress calculation example
    total_xp = 1250
    current_xp = 500
    progress = (current_xp / total_xp) * 100
    print(f"\n>> OVERALL PROGRESS: {progress:.1f}% TO LEVEL 2 (Senior Audio Lead)")
    print("="*60)

if __name__ == "__main__":
    main()
