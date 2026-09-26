import random
import time


def slow_print(text, delay=0.03):
    """逐字打印效果，让游戏更有代入感"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def game_intro():
    """游戏开场介绍"""
    slow_print("\n" + "=" * 50)
    slow_print("🌟  森林宝藏冒险  🌟")
    slow_print("=" * 50)
    slow_print("\n你是一位勇敢的冒险家，听说迷雾森林深处隐藏着传说中的宝藏...")
    slow_print("但森林中充满了未知的危险和谜题。")
    slow_print("\n你的任务：在3天内找到宝藏并活着离开！")
    slow_print("\n游戏规则：")
    slow_print("  - 每天你可以选择一个方向探索")
    slow_print("  - 不同的选择会导致不同的结果")
    slow_print("  - 你的生命值为100，遇到危险会减少")
    slow_print("  - 生命值归零则游戏结束")
    slow_print("\n祝你好运，冒险家！\n")
    input("按 Enter 键开始游戏...")


def day_event(day, health, inventory):
    """每天发生的事件"""
    slow_print(f"\n{'=' * 40}")
    slow_print(f"🌅  第 {day} 天  🌅")
    slow_print(f"❤️  当前生命值: {health}")
    slow_print(f"🎒  背包物品: {inventory if inventory else '空'}")
    slow_print(f"{'=' * 40}")

    events = [
        "森林",
        "河流",
        "山洞",
        "废弃小屋"
    ]

    print("\n你来到了一个分岔路口，你可以选择：")
    for i, loc in enumerate(events, 1):
        print(f"  {i}. 进入{loc}")

    while True:
        try:
            choice = int(input("\n请选择 (1-4): "))
            if 1 <= choice <= 4:
                break
            else:
                print("请输入1-4之间的数字！")
        except ValueError:
            print("请输入有效的数字！")

    return handle_event(events[choice - 1], health, inventory)


def handle_event(location, health, inventory):
    """处理各个地点的事件"""

    # 森林事件
    if location == "森林":
        events = [
            {"desc": "🌳 你遇到了一只友善的精灵！她给了你一个魔法苹果。",
             "health": +20, "item": "魔法苹果", "item_action": "add"},
            {"desc": "🐗 你惊动了一群野猪！被撞伤了。",
             "health": -15, "item": None},
            {"desc": "🍄 你发现了一片发光的蘑菇，吃了它感觉精力充沛！",
             "health": +10, "item": None},
            {"desc": "🌿 你不小心踩到了毒藤蔓，中毒了。",
             "health": -10, "item": None}
        ]

    # 河流事件
    elif location == "河流":
        events = [
            {"desc": "🎣 你在河边钓鱼，钓到了一条大鱼！补充了体力。",
             "health": +15, "item": None},
            {"desc": "💧 河水很清澈，你喝了水感觉神清气爽。",
             "health": +5, "item": None},
            {"desc": "🐊 一条鳄鱼突然出现！你奋力逃跑但被抓伤了。",
             "health": -20, "item": None},
            {"desc": "🧙 你遇到了一位老渔夫，他给了你一张藏宝图碎片。",
             "health": 0, "item": "藏宝图碎片", "item_action": "add"}
        ]

    # 山洞事件
    elif location == "山洞":
        events = [
            {"desc": "🦇 山洞里蝙蝠群突然飞出！你被咬伤了。",
             "health": -10, "item": None},
            {"desc": "💎 你发现了一颗发光的宝石！",
             "health": 0, "item": "发光宝石", "item_action": "add"},
            {"desc": "🐻 山洞里睡着一只熊，你悄悄溜走了。",
             "health": 0, "item": None},
            {"desc": "🔥 你发现了前人留下的篝火，休息后恢复了体力。",
             "health": +25, "item": None}
        ]

    # 废弃小屋事件
    else:  # 废弃小屋
        events = [
            {"desc": "📜 你在桌上发现了一本日记，里面记录了宝藏的位置！",
             "health": 0, "item": "藏宝图碎片", "item_action": "add"},
            {"desc": "🧪 你找到了一瓶治疗药水。",
             "health": 0, "item": "治疗药水", "item_action": "add"},
            {"desc": "👻 小屋里有鬼魂！你被吓得不轻。",
             "health": -5, "item": None},
            {"desc": "🗝️ 你找到了一把古老的钥匙。",
             "health": 0, "item": "古老钥匙", "item_action": "add"}
        ]

    # 随机选择一个事件
    event = random.choice(events)

    slow_print(f"\n{event['desc']}")
    time.sleep(1)

    # 处理生命值变化
    new_health = health + event['health']
    if event['health'] > 0:
        slow_print(f"✨ 生命值 +{event['health']}")
    elif event['health'] < 0:
        slow_print(f"💔 生命值 {event['health']}")

    # 处理物品
    if event.get('item'):
        if event.get('item_action') == 'add':
            inventory.append(event['item'])
            slow_print(f"🎁 获得物品: {event['item']}!")

    return max(0, min(100, new_health)), inventory


def check_treasure(health, inventory, day):
    """检查是否找到宝藏"""
    # 收集齐3张藏宝图碎片，或者第3天随机触发
    treasure_pieces = inventory.count("藏宝图碎片")

    if treasure_pieces >= 3:
        slow_print("\n✨✨✨ 你收集齐了藏宝图碎片！✨✨✨")
        slow_print("根据地图指引，你找到了宝藏的准确位置...")
        return True
    elif day >= 3 and random.random() < 0.3:
        slow_print("\n🔍 你无意中踩到了一块松动的地板...")
        return True
    elif "发光宝石" in inventory and "古老钥匙" in inventory:
        slow_print("\n🔑 宝石和钥匙产生了共鸣，打开了一扇隐藏的门！")
        return True

    return False


def boss_fight(health, inventory):
    """最终Boss战"""
    slow_print("\n" + "=" * 50)
    slow_print("👾  警告！森林守护者出现了！  👾")
    slow_print("=" * 50)
    slow_print("\n一只巨大的树精挡住了通往宝藏的路！")
    slow_print("树精的生命值: 50")

    boss_health = 50

    while boss_health > 0 and health > 0:
        print(f"\n你的生命值: {health} | 树精生命值: {boss_health}")
        print("\n你可以：")
        print("  1. ⚔️  攻击 (造成10-20伤害)")
        print("  2. 🛡️  防御 (减少50%受到的伤害)")
        print("  3. 💊  使用物品")

        choice = input("\n请选择 (1-3): ")

        # 初始化防御标志
        defend = False

        # 玩家行动
        if choice == "1":
            damage = random.randint(10, 20)
            boss_health -= damage
            slow_print(f"\n你挥剑攻击！造成了 {damage} 点伤害！")
        elif choice == "2":
            defend = True
            slow_print(f"\n你举起盾牌防御！")
        elif choice == "3":
            used_item = False
            if "治疗药水" in inventory:
                heal = random.randint(20, 40)
                health = min(100, health + heal)
                inventory.remove("治疗药水")
                slow_print(f"\n你喝下了治疗药水！恢复了 {heal} 点生命值！")
                used_item = True
            elif "魔法苹果" in inventory:
                heal = random.randint(15, 30)
                health = min(100, health + heal)
                inventory.remove("魔法苹果")
                slow_print(f"\n你吃下了魔法苹果！恢复了 {heal} 点生命值！")
                used_item = True
            else:
                slow_print("\n你没有可用的物品！")
                continue

            # 如果使用了物品，树精也会反击
            if used_item and boss_health > 0:
                boss_damage = random.randint(10, 25)
                slow_print(f"树精趁你使用物品时攻击！你受到了 {boss_damage} 点伤害！")
                health -= boss_damage
                time.sleep(1)
            continue
        else:
            slow_print("无效的选择！")
            continue

        # 树精反击（只在树精还活着时）
        if boss_health > 0:
            boss_damage = random.randint(10, 25)
            if defend:
                boss_damage = boss_damage // 2
                slow_print(f"树精攻击！但由于防御，只受到了 {boss_damage} 点伤害！")
            else:
                slow_print(f"树精攻击！你受到了 {boss_damage} 点伤害！")
            health -= boss_damage

        time.sleep(1)

    return health > 0


def game_ending(win, health, inventory):
    """游戏结局"""
    slow_print("\n" + "=" * 50)
    if win:
        slow_print("🎉🎉🎉  恭喜！你找到了传说中的宝藏！ 🎉🎉🎉")
        slow_print("=" * 50)
        slow_print("\n你打开了宝箱，里面装满了金币和魔法物品！")
        slow_print(f"你最终生命值: {health}")
        slow_print(f"你收集的物品: {inventory}")
        slow_print("\n你成为了著名的冒险家，这个故事在各地传颂...")
        slow_print("\n✨ 完美结局 ✨")
    elif health <= 0:
        slow_print("💀💀💀  游戏结束：你倒在了森林中... 💀💀💀")
        slow_print("=" * 50)
        slow_print("\n你的冒险以悲剧告终，没有人知道你去了哪里...")
        slow_print("\n☠️  死亡结局  ☠️")
    else:
        slow_print("😔  游戏结束：时间耗尽，你没能找到宝藏... 😔")
        slow_print("=" * 50)
        slow_print("\n你不得不空手离开迷雾森林，这次冒险失败了。")
        slow_print("\n📖  未完待续...  📖")

    print(f"\n你存活了3天")
    print(f"最终生命值: {health}")
    print(f"收集的物品: {len(inventory)} 件")


def main():
    """主游戏循环"""
    game_intro()

    health = 100
    inventory = []

    # 3天的游戏时间
    for day in range(1, 4):
        health, inventory = day_event(day, health, inventory)

        # 检查是否死亡
        if health <= 0:
            game_ending(False, health, inventory)
            return

        # 检查是否找到宝藏
        if check_treasure(health, inventory, day):
            slow_print("\n🏆 你发现了宝藏的入口！🏆")

            # 最终Boss战
            if boss_fight(health, inventory):
                game_ending(True, health, inventory)
            else:
                slow_print("\n💀 你没能打败森林守护者，倒在了宝藏前... 💀")
                game_ending(False, health, inventory)
            return

        if day < 3:
            slow_print("\n天色已晚，你搭起帐篷休息...")
            time.sleep(1)

    # 第三天结束还没找到宝藏
    game_ending(False, health, inventory)


# 运行游戏
if __name__ == "__main__":
    main()