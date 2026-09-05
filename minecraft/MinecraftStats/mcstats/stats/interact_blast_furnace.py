from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'interact_blast_furnace',
        {
            'title': '融化廠廠主',
            'desc': '使用鼓風爐的次數',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:interact_with_blast_furnace']),
        1919 # blast furnace usable since 18w50a
    ))
