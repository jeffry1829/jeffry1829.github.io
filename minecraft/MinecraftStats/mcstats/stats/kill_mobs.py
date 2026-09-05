from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_any',
        {
            'title': '擊殺領域！',
            'desc': '總共殺過的怪物數量',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:mob_kills'])
    ))

def create_kill_stat(mobId, title, mobText, minVersion = 0):
    mcstats.registry.append(
        mcstats.MinecraftStat(
            'kill_' + mobId,
            {
                'title': title,
                'desc': '總共殺過的' + mobText + '數量',
                'unit': 'int',
            },
            mcstats.StatReader(['minecraft:killed','minecraft:' + mobId]),
            minVersion
        ))

# Hostiles
create_kill_stat('blaze','滅火器','烈焰神')
create_kill_stat('creeper','苦力怕主宰','苦力怕')
create_kill_stat('endermite','滅蟎專家','終界蟎')
create_kill_stat('ender_dragon','屠龍者','終界龍')
create_kill_stat('ghast','眼淚收集者','地獄幽靈')
create_kill_stat('magma_cube','岩漿冰淇淋','地獄史萊姆')
create_kill_stat('phantom','夜魅射手','夜魅',1467) # added in 18w07a
# Note: Ravagers had been added as Illager Beats in 18w43a (1901)
# support for that snapshot may be added on demand
create_kill_stat('ravager','突襲！','劫毀獸',1930) # changed in 19w05a
create_kill_stat('shulker','開蚌專家','界伏蚌')
create_kill_stat('silverfish','可惡的小東西...','蠹魚')
create_kill_stat('slime','好黏！','史萊姆')
create_kill_stat('vex','惱鬼獵手','惱鬼')
create_kill_stat('witch','女巫獵人','女巫')
create_kill_stat('wither_skeleton','凋零骷髏獵手','凋零骷髏')

# Neutrals
create_kill_stat('bee','嗡嗡嗡','蜜蜂',2200) # added in 19w34a
create_kill_stat('dolphin','海豚獵手','海豚',1482) # added in 18w15a
create_kill_stat('enderman','安德終結者','終界使者')
create_kill_stat('iron_golem','守衛系統下線！','鐵傀儡')
create_kill_stat('panda','功夫熊貓','熊貓',1901) # added in 18w43a
create_kill_stat('polar_bear','北極熊盜獵者','北極熊')
create_kill_stat('snow_golem','反對雪地！','雪人')
create_kill_stat('zombie_pigman','地獄群架','地獄屍人')

# Passives
create_kill_stat('bat','蝙蝠獵手','蝙蝠')
create_kill_stat('chicken','烤雞手','雞')
create_kill_stat('cow','屠牛夫','牛')
create_kill_stat('horse','馬屠手','馬')
create_kill_stat('fox','フブキ フブキ フブキ！','狐狸',1932) # added in 19w07a
create_kill_stat('mooshroom','蘑菇肉愛好者','蘑菇牛')
create_kill_stat('parrot','笨鳥！','鸚鵡')
create_kill_stat('pig','屠夫','豬')
create_kill_stat('rabbit','兔子殺手','兔子')
create_kill_stat('sheep','大野狼','羊')
create_kill_stat('squid','池子清理者','烏賊')
create_kill_stat('turtle','馬力歐','烏龜',1467) # added in 18w07a
create_kill_stat('villager','獨裁者','村民')
create_kill_stat('wandering_trader','商人制裁者','流浪商人',1930) # added in 19w05a
create_kill_stat('wolf','壞狗！','狼/狗')

# Cats (including ozelots)
mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_ocelot',
        {
            'title': '屠貓者',
            'desc': '殺過的山貓/貓的數量',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:killed','minecraft:cat']),
            mcstats.StatReader(['minecraft:killed','minecraft:ocelot']),
        ])
    ))

# Llamas (including trader llamas)
mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_llama',
        {
            'title': '山賊',
            'desc': '殺過的羊駝數量',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:killed','minecraft:llama']),
            mcstats.StatReader(['minecraft:killed','minecraft:trader_llama']),
        ])
    ))

# Zombies (including Husks and Zombie Villagers)
mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_zombie',
        {
            'title': '殭屍碾碎機',
            'desc': '殺過的殭屍數量',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:killed','minecraft:husk']),
            mcstats.StatReader(['minecraft:killed','minecraft:drowned']),
            mcstats.StatReader(['minecraft:killed','minecraft:zombie']),
            mcstats.StatReader(['minecraft:killed','minecraft:zombie_villager']),
        ])
    ))

# Skeletons (including Strays)
mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_skeleton',
        {
            'title': '骨頭收集家',
            'desc': '殺過的骷髏弓箭手數量',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:killed','minecraft:skeleton']),
            mcstats.StatReader(['minecraft:killed','minecraft:stray']),
        ])
    ))

# Spiders (including Cave Spiders)
mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_spider',
        {
            'title': '蜘蛛恐懼症',
            'desc': '殺過的蜘蛛數量',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:killed','minecraft:spider']),
            mcstats.StatReader(['minecraft:killed','minecraft:cave_spider']),
        ])
    ))

# Guardians (including Elder Guardians)
mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_guardian',
        {
            'title': '深海突襲者',
            'desc': '殺過的深海守衛數量',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:killed','minecraft:guardian']),
            mcstats.StatReader(['minecraft:killed','minecraft:elder_guardian']),
        ])
    ))

# Illagers (all types)
mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_illagers',
        {
            'title': '清除者',
            'desc': '殺過的窳民數量',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:killed','minecraft:evoker']),
            mcstats.StatReader(['minecraft:killed','minecraft:vindicator']),
            mcstats.StatReader(['minecraft:killed','minecraft:pillager']),
            mcstats.StatReader(['minecraft:killed','minecraft:illusioner']),
            mcstats.StatReader(['minecraft:killed','minecraft:illager_beast']),
        ])
    ))

# Fish mobs
mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_fish',
        {
            'title': '捕魚專家',
            'desc': '殺過的魚的數量',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:killed','minecraft:cod']),
            mcstats.StatReader(['minecraft:killed','minecraft:salmon']),
            mcstats.StatReader(['minecraft:killed','minecraft:pufferfish']),
            mcstats.StatReader(['minecraft:killed','minecraft:tropical_fish']),
        ]),
        1471 # fish mobs added in 18w08b
    ))
