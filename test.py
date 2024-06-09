import asyncio
import coc 

client = coc.Client()

async def main():
        await client.login(email="tadat216@gmail.com",password="zx1478956230")

        player_data = await client.get_player("QL8L88QQQ")
        # home_troops = player_data.troops
        # for troop in home_troops:
        #         print(troop.name, troop.get_max_level_for_townhall(12), troop.is_super_troop)
        home_hero = player_data.heroes
        
        #for hero in client.get_hero("Babarian King"):
        #         print(hero.name, hero.level, hero.get_max_level_for_townhall(12), hero._is_home_village, hero.equipment)
        # print(player_data.name, player_data.league.icon.tiny)
        #queen = client.get_hero("Archer Queen")
        #cost = queen.upgrade_cost
        #for i in range(queen.get_max_level_for_townhall(16)):
        #   print(cost[i+1])
        #clan = player_data.clan
        #print(clan.badge)
        #achivements = player_data.achievements
        #for achivement in achivements:
        #        if achivement.village == 'clanCapital':
        #                print(achivement.name, achivement.village, achivement.value, achivement.target)
        #achivement = player_data.get_achievement('Aggressive Capitalism')
        # leagues = await client.search_leagues()
        # for league in leagues:
        #         stat = await client.get_league(league.id)
        #         print(stat.icon)
        print(player_data.role)
        await client.close()

asyncio.run(main())
