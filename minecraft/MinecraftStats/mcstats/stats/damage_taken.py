from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'damage_taken',
        {
            'title': '沙包',
            'desc': '受過的傷害值',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:damage_taken'])
    ))
