from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'play_record',
        {
            'title': '欣賞家',
            'desc': '聽CD的數量',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:play_record'])
    ))
