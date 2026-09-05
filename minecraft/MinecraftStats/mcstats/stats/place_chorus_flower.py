from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_chorus_flower',
        {
            'title': '歌萊花農',
            'desc': '種過的歌萊花數量',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:chorus_flower'])
    ))
