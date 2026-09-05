from mcstats import mcstats

def create_ore_stat(title, oreId, oreName):
    mcstats.registry.append(
        mcstats.MinecraftStat(
            'mine_' + oreId + '_ore',
            {
                'title': title,
                'desc': '挖過的' + oreName + '礦的數量',
                'unit': 'int',
            },
            mcstats.StatReader(['minecraft:mined','minecraft:' + oreId + '_ore'])
        ))

create_ore_stat('黑金', 'coal', '石炭')
create_ore_stat('鋼鐵之心', 'iron', '鐵')
create_ore_stat('黃金衝刺', 'gold', '金')
create_ore_stat('鑽石！', 'diamond', '鑽石')
create_ore_stat('高山礦工', 'emerald', '綠寶石')
create_ore_stat('藍礦工', 'lapis', '青金石')
create_ore_stat('紅石礦工', 'redstone', '紅石')
create_ore_stat('石英礦工', 'nether_quartz', '石英')
