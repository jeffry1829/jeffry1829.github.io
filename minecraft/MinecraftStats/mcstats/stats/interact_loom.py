from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'interact_loom',
        {
            'title': '紡織工',
            'desc': '使用織布機的次數',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:interact_with_loom']),
        1901 # looms added in 18w43a
    ))
