from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'biomes',
        {
            'title': '探險家',
            'desc': '探索過的生態域',
            'unit': 'int',
        },
        mcstats.StatListLengthReader([
            'advancements',
            'minecraft:adventure/adventuring_time',
            'criteria'
        ])
    ))
