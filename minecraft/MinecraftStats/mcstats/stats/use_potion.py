from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_potion',
        {
            'title': '煉金術士',
            'desc': '藥水使用次數',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:used','minecraft:lingering_potion']),
            mcstats.StatReader(['minecraft:used','minecraft:potion']),
            mcstats.StatReader(['minecraft:used','minecraft:splash_potion'])
        ])
    ))
