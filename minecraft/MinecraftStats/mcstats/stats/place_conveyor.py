from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_conveyor',
        {
            'title': '傳輸家',
            'desc': '放置的漏斗和投擲器數量',
            'unit': 'int',
        },
        mcstats.StatDiffReader(
            mcstats.StatSumMatchReader(
                ['minecraft:used'],
                ['minecraft:hopper','minecraft:dropper']),
            mcstats.StatSumMatchReader(
                ['minecraft:mined'],
                ['minecraft:hopper','minecraft:dropper']),
        )
    ))
