from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_bookshelf',
        {
            'title': '圖書館員',
            'desc': '造過的書櫃數量',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:bookshelf'])
    ))
