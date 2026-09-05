from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'killed_by_creeper',
        {
            'title': '阿！！！',
            'desc': '被苦力帕殺的次數',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:killed_by','minecraft:creeper'])
    ))
