from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'eat_junkfood',
        {
            'title': '垃圾桶',
            'desc': '吃過的垃圾食物數量',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:used','minecraft:rotten_flesh']),
            mcstats.StatReader(['minecraft:used','minecraft:spider_eye']),
            mcstats.StatReader(['minecraft:used','minecraft:poisonous_potato']),
        ])
    ))
