from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_bars',
        {
            'title': '獄卒',
            'desc': '鐵欄杆的放置數量',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:iron_bars'])
    ))
