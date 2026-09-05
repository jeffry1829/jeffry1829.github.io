from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_obsidian',
        {
            'title': '黑曜礦工',
            'desc': '挖過的黑曜石數量',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:mined','minecraft:obsidian'])
    ))
