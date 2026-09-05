from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'enchant',
        {
            'title': '附魔師',
            'desc': '附魔的物品數量',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:enchant_item'])
    ))
