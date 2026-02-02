# OpenDota, on the other hand does!
**URL:** https://docs.opendota.com
**Page Title:** OpenDota API
--------------------

- Introduction
- matches get GET /matches/{match_id}
- get GET /matches/{match_id}
- players get GET /players/{account_id} get GET /players/{account_id}/wl get GET /players/{account_id}/recentMatches get GET /players/{account_id}/matches get GET /players/{account_id}/heroes get GET /players/{account_id}/peers get GET /players/{account_id}/pros get GET /players/{account_id}/totals get GET /players/{account_id}/counts get GET /players/{account_id}/histograms get GET /players/{account_id}/wardmap get GET /players/{account_id}/wordcloud get GET /players/{account_id}/ratings get GET /players/{account_id}/rankings post POST /players/{account_id}/refresh
- get GET /players/{account_id}
- get GET /players/{account_id}/wl
- get GET /players/{account_id}/recentMatches
- get GET /players/{account_id}/matches
- get GET /players/{account_id}/heroes
- get GET /players/{account_id}/peers
- get GET /players/{account_id}/pros
- get GET /players/{account_id}/totals
- get GET /players/{account_id}/counts
- get GET /players/{account_id}/histograms
- get GET /players/{account_id}/wardmap
- get GET /players/{account_id}/wordcloud
- get GET /players/{account_id}/ratings
- get GET /players/{account_id}/rankings
- post POST /players/{account_id}/refresh
- top players get GET /topPlayers
- get GET /topPlayers
- pro players get GET /proPlayers
- get GET /proPlayers
- pro matches get GET /proMatches
- get GET /proMatches
- public matches get GET /publicMatches
- get GET /publicMatches
- parsed matches get GET /parsedMatches
- get GET /parsedMatches
- explorer get GET /explorer
- get GET /explorer
- metadata get GET /metadata
- get GET /metadata
- distributions get GET /distributions
- get GET /distributions
- search get GET /search
- get GET /search
- rankings get GET /rankings
- get GET /rankings
- benchmarks get GET /benchmarks
- get GET /benchmarks
- health get GET /health
- get GET /health
- request get GET /request/{jobId} post POST /request/{match_id}
- get GET /request/{jobId}
- post POST /request/{match_id}
- findMatches get GET /
- get GET /
- heroes get GET /heroes get GET /heroes/{hero_id}/matches get GET /heroes/{hero_id}/matchups get GET /heroes/{hero_id}/durations get GET /heroes/{hero_id}/players get GET /heroes/{hero_id}/itemPopularity
- get GET /heroes
- get GET /heroes/{hero_id}/matches
- get GET /heroes/{hero_id}/matchups
- get GET /heroes/{hero_id}/durations
- get GET /heroes/{hero_id}/players
- get GET /heroes/{hero_id}/itemPopularity
- hero stats get GET /heroStats
- get GET /heroStats
- leagues get GET /leagues get GET /leagues/{league_id} get GET /leagues/{league_id}/matches get GET /leagues/{league_id}/matchIds get GET /leagues/{league_id}/teams
- get GET /leagues
- get GET /leagues/{league_id}
- get GET /leagues/{league_id}/matches
- get GET /leagues/{league_id}/matchIds
- get GET /leagues/{league_id}/teams
- teams get GET /teams get GET /teams/{team_id} get GET /teams/{team_id}/matches get GET /teams/{team_id}/players get GET /teams/{team_id}/heroes
- get GET /teams
- get GET /teams/{team_id}
- get GET /teams/{team_id}/matches
- get GET /teams/{team_id}/players
- get GET /teams/{team_id}/heroes
- records get GET /records/{field}
- get GET /records/{field}
- live get GET /live
- get GET /live
- scenarios get GET /scenarios/itemTimings get GET /scenarios/laneRoles get GET /scenarios/misc
- get GET /scenarios/itemTimings
- get GET /scenarios/laneRoles
- get GET /scenarios/misc
- schema get GET /schema
- get GET /schema
- constants get GET /constants
- get GET /constants

## OpenDota API (31.1.0)

Download OpenAPI specification: Download
[LINK: Download](https://api.opendota.com/api)

## Introduction

The OpenDota API provides Dota 2 related data including advanced match data extracted from match replays.
You can find data that can be used to convert hero and ability IDs and other information provided by the API from the dotaconstants repository.
[LINK: dotaconstants](https://github.com/odota/dotaconstants)
You can use the API without a key, but registering for a key allows increased rate limits and usage. Check out the API page to learn more.
[LINK: API page](https://www.opendota.com/api-keys)

## matches

## GET /matches/{match_id}

Match data

### Responses

### Response samples

- 200
- "match_id" : 3703866531 ,
- "barracks_status_dire" : 0 ,
- "barracks_status_radiant" : 0 ,
- "chat" : [ { "time" : 0 , "unit" : "string" , "key" : "string" , "slot" : 0 , "player_slot" : 0 } ] ,
- { "time" : 0 , "unit" : "string" , "key" : "string" , "slot" : 0 , "player_slot" : 0 }
- "time" : 0 ,
- "unit" : "string" ,
- "key" : "string" ,
- "slot" : 0 ,
- "player_slot" : 0
- "cluster" : 0 ,
- "cosmetics" : { "property1" : 0 , "property2" : 0 } ,
- "property1" : 0 ,
- "property2" : 0
- "dire_score" : 0 ,
- "draft_timings" : [ { "order" : 0 , "pick" : true , "active_team" : 0 , "hero_id" : 0 , "player_slot" : 0 , "extra_time" : 0 , "total_time_taken" : 0 } ] ,
- { "order" : 0 , "pick" : true , "active_team" : 0 , "hero_id" : 0 , "player_slot" : 0 , "extra_time" : 0 , "total_time_taken" : 0 }
- "order" : 0 ,
- "pick" : true ,
- "active_team" : 0 ,
- "hero_id" : 0 ,
- "player_slot" : 0 ,
- "extra_time" : 0 ,
- "total_time_taken" : 0
- "duration" : 0 ,
- "engine" : 0 ,
- "first_blood_time" : 0 ,
- "game_mode" : 0 ,
- "human_players" : 0 ,
- "leagueid" : 0 ,
- "lobby_type" : 0 ,
- "match_seq_num" : 0 ,
- "negative_votes" : 0 ,
- "objectives" : [ { } ] ,
- { }
- "picks_bans" : [ { "is_pick" : true , "hero_id" : 0 , "team" : 0 , "order" : 0 } ] ,
- { "is_pick" : true , "hero_id" : 0 , "team" : 0 , "order" : 0 }
- "is_pick" : true ,
- "hero_id" : 0 ,
- "team" : 0 ,
- "order" : 0
- "positive_votes" : 0 ,
- "radiant_gold_adv" : [ 0 ] ,
- "radiant_score" : 0 ,
- "radiant_win" : true ,
- "radiant_xp_adv" : [ 0 ] ,
- "start_time" : 0 ,
- "teamfights" : [ { } ] ,
- { }
- "tower_status_dire" : 0 ,
- "tower_status_radiant" : 0 ,
- "version" : 0 ,
- "replay_salt" : 0 ,
- "series_id" : 0 ,
- "series_type" : 0 ,
- "radiant_team" : { } ,
- "dire_team" : { } ,
- "league" : { } ,
- "skill" : 0 ,
- "players" : [ { "match_id" : 3703866531 , "player_slot" : 0 , "ability_upgrades_arr" : [ 0 ] , "ability_uses" : { } , "ability_targets" : { } , "damage_targets" : { } , "account_id" : 0 , "actions" : { } , "additional_units" : [ { } ] , "assists" : 0 , "backpack_0" : 0 , "backpack_1" : 0 , "backpack_2" : 0 , "buyback_log" : [ { "time" : 0 , "slot" : 0 , "player_slot" : 0 } ] , "camps_stacked" : 0 , "connection_log" : [ { "time" : 0 , "event" : "string" , "player_slot" : 0 } ] , "creeps_stacked" : 0 , "damage" : { } , "damage_inflictor" : { } , "damage_inflictor_received" : { } , "damage_taken" : { } , "deaths" : 0 , "denies" : 0 , "dn_t" : [ 0 ] , "gold" : 0 , "gold_per_min" : 0 , "gold_reasons" : { } , "gold_spent" : 0 , "gold_t" : [ 0 ] , "hero_damage" : 0 , "hero_healing" : 0 , "hero_hits" : { } , "hero_id" : 0 , "item_0" : 0 , "item_1" : 0 , "item_2" : 0 , "item_3" : 0 , "item_4" : 0 , "item_5" : 0 , "item_uses" : { } , "kill_streaks" : { } , "killed" : { } , "killed_by" : { } , "kills" : 0 , "kills_log" : [ { "time" : 0 , "key" : "string" } ] , "lane_pos" : { } , "last_hits" : 0 , "leaver_status" : 0 , "level" : 0 , "lh_t" : [ 0 ] , "life_state" : { } , "max_hero_hit" : { } , "multi_kills" : { } , "obs" : { } , "obs_left_log" : [ { } ] , "obs_log" : [ { } ] , "obs_placed" : 0 , "party_id" : 0 , "permanent_buffs" : [ { } ] , "hero_variant" : 0 , "pings" : 0 , "purchase" : { } , "purchase_log" : [ { "time" : 0 , "key" : "string" , "charges" : 0 } ] , "rune_pickups" : 0 , "runes" : { "property1" : 0 , "property2" : 0 } , "runes_log" : [ { "time" : 0 , "key" : 0 } ] , "sen" : { } , "sen_left_log" : [ { } ] , "sen_log" : [ { } ] , "sen_placed" : 0 , "stuns" : 0 , "times" : [ 0 ] , "tower_damage" : 0 , "xp_per_min" : 0 , "xp_reasons" : { } , "xp_t" : [ 0 ] , "personaname" : "420 booty wizard" , "name" : "string" , "last_login" : "2019-08-24T14:15:22Z" , "radiant_win" : true , "start_time" : 0 , "duration" : 0 , "cluster" : 0 , "lobby_type" : 0 , "game_mode" : 0 , "patch" : 0 , "region" : 0 , "isRadiant" : true , "win" : 0 , "lose" : 0 , "total_gold" : 0 , "total_xp" : 0 , "kills_per_min" : 0 , "kda" : 0 , "abandons" : 0 , "neutral_kills" : 0 , "tower_kills" : 0 , "courier_kills" : 0 , "lane_kills" : 0 , "hero_kills" : 0 , "observer_kills" : 0 , "sentry_kills" : 0 , "roshan_kills" : 0 , "necronomicon_kills" : 0 , "ancient_kills" : 0 , "buyback_count" : 0 , "observer_uses" : 0 , "sentry_uses" : 0 , "lane_efficiency" : 0 , "lane_efficiency_pct" : 0 , "lane" : 0 , "lane_role" : 0 , "is_roaming" : true , "purchase_time" : { } , "first_purchase_time" : { } , "item_win" : { } , "item_usage" : { } , "purchase_tpscroll" : 0 , "actions_per_min" : 0 , "life_state_dead" : 0 , "rank_tier" : 0 , "cosmetics" : [ { "item_id" : 0 , "name" : "string" , "prefab" : "string" , "creation_date" : "2019-08-24T14:15:22Z" , "image_inventory" : "string" , "image_path" : "string" , "item_description" : "string" , "item_name" : "string" , "item_rarity" : "string" , "item_type_name" : "string" , "used_by_heroes" : "string" } ] , "benchmarks" : { } , "neutral_tokens_log" : [ { "time" : 0 , "key" : "string" } ] , "neutral_item_history" : [ { "time" : 0 , "item_neutral" : "string" , "item_neutral_enhancement" : "string" } ] } ] ,
- { "match_id" : 3703866531 , "player_slot" : 0 , "ability_upgrades_arr" : [ 0 ] , "ability_uses" : { } , "ability_targets" : { } , "damage_targets" : { } , "account_id" : 0 , "actions" : { } , "additional_units" : [ { } ] , "assists" : 0 , "backpack_0" : 0 , "backpack_1" : 0 , "backpack_2" : 0 , "buyback_log" : [ { "time" : 0 , "slot" : 0 , "player_slot" : 0 } ] , "camps_stacked" : 0 , "connection_log" : [ { "time" : 0 , "event" : "string" , "player_slot" : 0 } ] , "creeps_stacked" : 0 , "damage" : { } , "damage_inflictor" : { } , "damage_inflictor_received" : { } , "damage_taken" : { } , "deaths" : 0 , "denies" : 0 , "dn_t" : [ 0 ] , "gold" : 0 , "gold_per_min" : 0 , "gold_reasons" : { } , "gold_spent" : 0 , "gold_t" : [ 0 ] , "hero_damage" : 0 , "hero_healing" : 0 , "hero_hits" : { } , "hero_id" : 0 , "item_0" : 0 , "item_1" : 0 , "item_2" : 0 , "item_3" : 0 , "item_4" : 0 , "item_5" : 0 , "item_uses" : { } , "kill_streaks" : { } , "killed" : { } , "killed_by" : { } , "kills" : 0 , "kills_log" : [ { "time" : 0 , "key" : "string" } ] , "lane_pos" : { } , "last_hits" : 0 , "leaver_status" : 0 , "level" : 0 , "lh_t" : [ 0 ] , "life_state" : { } , "max_hero_hit" : { } , "multi_kills" : { } , "obs" : { } , "obs_left_log" : [ { } ] , "obs_log" : [ { } ] , "obs_placed" : 0 , "party_id" : 0 , "permanent_buffs" : [ { } ] , "hero_variant" : 0 , "pings" : 0 , "purchase" : { } , "purchase_log" : [ { "time" : 0 , "key" : "string" , "charges" : 0 } ] , "rune_pickups" : 0 , "runes" : { "property1" : 0 , "property2" : 0 } , "runes_log" : [ { "time" : 0 , "key" : 0 } ] , "sen" : { } , "sen_left_log" : [ { } ] , "sen_log" : [ { } ] , "sen_placed" : 0 , "stuns" : 0 , "times" : [ 0 ] , "tower_damage" : 0 , "xp_per_min" : 0 , "xp_reasons" : { } , "xp_t" : [ 0 ] , "personaname" : "420 booty wizard" , "name" : "string" , "last_login" : "2019-08-24T14:15:22Z" , "radiant_win" : true , "start_time" : 0 , "duration" : 0 , "cluster" : 0 , "lobby_type" : 0 , "game_mode" : 0 , "patch" : 0 , "region" : 0 , "isRadiant" : true , "win" : 0 , "lose" : 0 , "total_gold" : 0 , "total_xp" : 0 , "kills_per_min" : 0 , "kda" : 0 , "abandons" : 0 , "neutral_kills" : 0 , "tower_kills" : 0 , "courier_kills" : 0 , "lane_kills" : 0 , "hero_kills" : 0 , "observer_kills" : 0 , "sentry_kills" : 0 , "roshan_kills" : 0 , "necronomicon_kills" : 0 , "ancient_kills" : 0 , "buyback_count" : 0 , "observer_uses" : 0 , "sentry_uses" : 0 , "lane_efficiency" : 0 , "lane_efficiency_pct" : 0 , "lane" : 0 , "lane_role" : 0 , "is_roaming" : true , "purchase_time" : { } , "first_purchase_time" : { } , "item_win" : { } , "item_usage" : { } , "purchase_tpscroll" : 0 , "actions_per_min" : 0 , "life_state_dead" : 0 , "rank_tier" : 0 , "cosmetics" : [ { "item_id" : 0 , "name" : "string" , "prefab" : "string" , "creation_date" : "2019-08-24T14:15:22Z" , "image_inventory" : "string" , "image_path" : "string" , "item_description" : "string" , "item_name" : "string" , "item_rarity" : "string" , "item_type_name" : "string" , "used_by_heroes" : "string" } ] , "benchmarks" : { } , "neutral_tokens_log" : [ { "time" : 0 , "key" : "string" } ] , "neutral_item_history" : [ { "time" : 0 , "item_neutral" : "string" , "item_neutral_enhancement" : "string" } ] }
- "match_id" : 3703866531 ,
- "player_slot" : 0 ,
- "ability_upgrades_arr" : [ 0 ] ,
- "ability_uses" : { } ,
- "ability_targets" : { } ,
- "damage_targets" : { } ,
- "account_id" : 0 ,
- "actions" : { } ,
- "additional_units" : [ { } ] ,
- { }
- "assists" : 0 ,
- "backpack_0" : 0 ,
- "backpack_1" : 0 ,
- "backpack_2" : 0 ,
- "buyback_log" : [ { "time" : 0 , "slot" : 0 , "player_slot" : 0 } ] ,
- { "time" : 0 , "slot" : 0 , "player_slot" : 0 }
- "time" : 0 ,
- "slot" : 0 ,
- "player_slot" : 0
- "camps_stacked" : 0 ,
- "connection_log" : [ { "time" : 0 , "event" : "string" , "player_slot" : 0 } ] ,
- { "time" : 0 , "event" : "string" , "player_slot" : 0 }
- "time" : 0 ,
- "event" : "string" ,
- "player_slot" : 0
- "creeps_stacked" : 0 ,
- "damage" : { } ,
- "damage_inflictor" : { } ,
- "damage_inflictor_received" : { } ,
- "damage_taken" : { } ,
- "deaths" : 0 ,
- "denies" : 0 ,
- "dn_t" : [ 0 ] ,
- "gold" : 0 ,
- "gold_per_min" : 0 ,
- "gold_reasons" : { } ,
- "gold_spent" : 0 ,
- "gold_t" : [ 0 ] ,
- "hero_damage" : 0 ,
- "hero_healing" : 0 ,
- "hero_hits" : { } ,
- "hero_id" : 0 ,
- "item_0" : 0 ,
- "item_1" : 0 ,
- "item_2" : 0 ,
- "item_3" : 0 ,
- "item_4" : 0 ,
- "item_5" : 0 ,
- "item_uses" : { } ,
- "kill_streaks" : { } ,
- "killed" : { } ,
- "killed_by" : { } ,
- "kills" : 0 ,
- "kills_log" : [ { "time" : 0 , "key" : "string" } ] ,
- { "time" : 0 , "key" : "string" }
- "time" : 0 ,
- "key" : "string"
- "lane_pos" : { } ,
- "last_hits" : 0 ,
- "leaver_status" : 0 ,
- "level" : 0 ,
- "lh_t" : [ 0 ] ,
- "life_state" : { } ,
- "max_hero_hit" : { } ,
- "multi_kills" : { } ,
- "obs" : { } ,
- "obs_left_log" : [ { } ] ,
- { }
- "obs_log" : [ { } ] ,
- { }
- "obs_placed" : 0 ,
- "party_id" : 0 ,
- "permanent_buffs" : [ { } ] ,
- { }
- "hero_variant" : 0 ,
- "pings" : 0 ,
- "purchase" : { } ,
- "purchase_log" : [ { "time" : 0 , "key" : "string" , "charges" : 0 } ] ,
- { "time" : 0 , "key" : "string" , "charges" : 0 }
- "time" : 0 ,
- "key" : "string" ,
- "charges" : 0
- "rune_pickups" : 0 ,
- "runes" : { "property1" : 0 , "property2" : 0 } ,
- "property1" : 0 ,
- "property2" : 0
- "runes_log" : [ { "time" : 0 , "key" : 0 } ] ,
- { "time" : 0 , "key" : 0 }
- "time" : 0 ,
- "key" : 0
- "sen" : { } ,
- "sen_left_log" : [ { } ] ,
- { }
- "sen_log" : [ { } ] ,
- { }
- "sen_placed" : 0 ,
- "stuns" : 0 ,
- "times" : [ 0 ] ,
- "tower_damage" : 0 ,
- "xp_per_min" : 0 ,
- "xp_reasons" : { } ,
- "xp_t" : [ 0 ] ,
- "personaname" : "420 booty wizard" ,
- "name" : "string" ,
- "last_login" : "2019-08-24T14:15:22Z" ,
- "radiant_win" : true ,
- "start_time" : 0 ,
- "duration" : 0 ,
- "cluster" : 0 ,
- "lobby_type" : 0 ,
- "game_mode" : 0 ,
- "patch" : 0 ,
- "region" : 0 ,
- "isRadiant" : true ,
- "win" : 0 ,
- "lose" : 0 ,
- "total_gold" : 0 ,
- "total_xp" : 0 ,
- "kills_per_min" : 0 ,
- "kda" : 0 ,
- "abandons" : 0 ,
- "neutral_kills" : 0 ,
- "tower_kills" : 0 ,
- "courier_kills" : 0 ,
- "lane_kills" : 0 ,
- "hero_kills" : 0 ,
- "observer_kills" : 0 ,
- "sentry_kills" : 0 ,
- "roshan_kills" : 0 ,
- "necronomicon_kills" : 0 ,
- "ancient_kills" : 0 ,
- "buyback_count" : 0 ,
- "observer_uses" : 0 ,
- "sentry_uses" : 0 ,
- "lane_efficiency" : 0 ,
- "lane_efficiency_pct" : 0 ,
- "lane" : 0 ,
- "lane_role" : 0 ,
- "is_roaming" : true ,
- "purchase_time" : { } ,
- "first_purchase_time" : { } ,
- "item_win" : { } ,
- "item_usage" : { } ,
- "purchase_tpscroll" : 0 ,
- "actions_per_min" : 0 ,
- "life_state_dead" : 0 ,
- "rank_tier" : 0 ,
- "cosmetics" : [ { "item_id" : 0 , "name" : "string" , "prefab" : "string" , "creation_date" : "2019-08-24T14:15:22Z" , "image_inventory" : "string" , "image_path" : "string" , "item_description" : "string" , "item_name" : "string" , "item_rarity" : "string" , "item_type_name" : "string" , "used_by_heroes" : "string" } ] ,
- { "item_id" : 0 , "name" : "string" , "prefab" : "string" , "creation_date" : "2019-08-24T14:15:22Z" , "image_inventory" : "string" , "image_path" : "string" , "item_description" : "string" , "item_name" : "string" , "item_rarity" : "string" , "item_type_name" : "string" , "used_by_heroes" : "string" }
- "item_id" : 0 ,
- "name" : "string" ,
- "prefab" : "string" ,
- "creation_date" : "2019-08-24T14:15:22Z" ,
- "image_inventory" : "string" ,
- "image_path" : "string" ,
- "item_description" : "string" ,
- "item_name" : "string" ,
- "item_rarity" : "string" ,
- "item_type_name" : "string" ,
- "used_by_heroes" : "string"
- "benchmarks" : { } ,
- "neutral_tokens_log" : [ { "time" : 0 , "key" : "string" } ] ,
- { "time" : 0 , "key" : "string" }
- "time" : 0 ,
- "key" : "string"
- "neutral_item_history" : [ { "time" : 0 , "item_neutral" : "string" , "item_neutral_enhancement" : "string" } ]
- { "time" : 0 , "item_neutral" : "string" , "item_neutral_enhancement" : "string" }
- "time" : 0 ,
- "item_neutral" : "string" ,
- "item_neutral_enhancement" : "string"
- "patch" : 0 ,
- "region" : 0 ,
- "all_word_counts" : { } ,
- "my_word_counts" : { } ,
- "throw" : 0 ,
- "comeback" : 0 ,
- "loss" : 0 ,
- "win" : 0 ,
- "replay_url" : "string" ,
- "pauses" : [ { "time" : 0 , "duration" : 0 } ]
- { "time" : 0 , "duration" : 0 }
- "time" : 0 ,
- "duration" : 0

## players

## GET /players/{account_id}

Player data
Steam32 account ID

### Responses

### Response samples

- 200
- "rank_tier" : 0 ,
- "leaderboard_rank" : 0 ,
- "computed_mmr" : 0 ,
- "computed_mmr_turbo" : 0 ,
- "aliases" : [ { "personaname" : "string" , "name_since" : "string" } ] ,
- { "personaname" : "string" , "name_since" : "string" }
- "personaname" : "string" ,
- "name_since" : "string"
- "profile" : { "account_id" : 0 , "personaname" : "420 booty wizard" , "name" : "string" , "plus" : true , "cheese" : 0 , "steamid" : "string" , "avatar" : "string" , "avatarmedium" : "string" , "avatarfull" : "string" , "profileurl" : "string" , "last_login" : "string" , "loccountrycode" : "string" , "is_contributor" : false , "is_subscriber" : false }
- "account_id" : 0 ,
- "personaname" : "420 booty wizard" ,
- "name" : "string" ,
- "plus" : true ,
- "cheese" : 0 ,
- "steamid" : "string" ,
- "avatar" : "string" ,
- "avatarmedium" : "string" ,
- "avatarfull" : "string" ,
- "profileurl" : "string" ,
- "last_login" : "string" ,
- "loccountrycode" : "string" ,
- "is_contributor" : false ,
- "is_subscriber" : false

## GET /players/{account_id}/wl

Win/Loss count
Steam32 account ID
Number of matches to limit to
Number of matches to offset start by
Whether the player won
Patch ID, from dotaconstants
Game Mode ID
Lobby type ID
Region ID
Days previous
Lane Role ID
Hero ID
Whether the player was radiant
Account IDs in the match (array)
Account IDs not in the match (array)
Hero IDs on the player's team (array)
Hero IDs against the player's team (array)
Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches.
The minimum number of games played, for filtering hero stats
The field to return matches sorted by in descending order

### Responses

### Response samples

- 200
- "win" : 0 ,
- "lose" : 0

## GET /players/{account_id}/recentMatches

Recent matches played (limited number of results)
Steam32 account ID

### Responses

### Response samples

- 200
- { }

## GET /players/{account_id}/matches

Matches played (full history, and supports column selection)
Steam32 account ID
Number of matches to limit to
Number of matches to offset start by
Whether the player won
Patch ID, from dotaconstants
Game Mode ID
Lobby type ID
Region ID
Days previous
Lane Role ID
Hero ID
Whether the player was radiant
Account IDs in the match (array)
Account IDs not in the match (array)
Hero IDs on the player's team (array)
Hero IDs against the player's team (array)
Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches.
The minimum number of games played, for filtering hero stats
The field to return matches sorted by in descending order
Fields to project (array)

### Responses

### Response samples

- 200
- { "match_id" : 3703866531 , "player_slot" : 0 , "radiant_win" : true , "duration" : 0 , "game_mode" : 0 , "lobby_type" : 0 , "hero_id" : 0 , "start_time" : 0 , "version" : 0 , "kills" : 0 , "deaths" : 0 , "assists" : 0 , "skill" : 0 , "average_rank" : 0 , "leaver_status" : 0 , "party_size" : 0 , "hero_variant" : 0 }
- "match_id" : 3703866531 ,
- "player_slot" : 0 ,
- "radiant_win" : true ,
- "duration" : 0 ,
- "game_mode" : 0 ,
- "lobby_type" : 0 ,
- "hero_id" : 0 ,
- "start_time" : 0 ,
- "version" : 0 ,
- "kills" : 0 ,
- "deaths" : 0 ,
- "assists" : 0 ,
- "skill" : 0 ,
- "average_rank" : 0 ,
- "leaver_status" : 0 ,
- "party_size" : 0 ,
- "hero_variant" : 0

## GET /players/{account_id}/heroes

Heroes played
Steam32 account ID
Number of matches to limit to
Number of matches to offset start by
Whether the player won
Patch ID, from dotaconstants
Game Mode ID
Lobby type ID
Region ID
Days previous
Lane Role ID
Hero ID
Whether the player was radiant
Account IDs in the match (array)
Account IDs not in the match (array)
Hero IDs on the player's team (array)
Hero IDs against the player's team (array)
Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches.
The minimum number of games played, for filtering hero stats
The field to return matches sorted by in descending order

### Responses

### Response samples

- 200
- { "hero_id" : 0 , "last_played" : 0 , "games" : 0 , "win" : 0 , "with_games" : 0 , "with_win" : 0 , "against_games" : 0 , "against_win" : 0 }
- "hero_id" : 0 ,
- "last_played" : 0 ,
- "games" : 0 ,
- "win" : 0 ,
- "with_games" : 0 ,
- "with_win" : 0 ,
- "against_games" : 0 ,
- "against_win" : 0

## GET /players/{account_id}/peers

Players played with
Steam32 account ID
Number of matches to limit to
Number of matches to offset start by
Whether the player won
Patch ID, from dotaconstants
Game Mode ID
Lobby type ID
Region ID
Days previous
Lane Role ID
Hero ID
Whether the player was radiant
Account IDs in the match (array)
Account IDs not in the match (array)
Hero IDs on the player's team (array)
Hero IDs against the player's team (array)
Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches.
The minimum number of games played, for filtering hero stats
The field to return matches sorted by in descending order

### Responses

### Response samples

- 200
- { "account_id" : 0 , "last_played" : 0 , "win" : 0 , "games" : 0 , "with_win" : 0 , "with_games" : 0 , "against_win" : 0 , "against_games" : 0 , "with_gpm_sum" : 0 , "with_xpm_sum" : 0 , "personaname" : "420 booty wizard" , "name" : "string" , "is_contributor" : true , "is_subscriber" : true , "last_login" : "string" , "avatar" : "string" , "avatarfull" : "string" }
- "account_id" : 0 ,
- "last_played" : 0 ,
- "win" : 0 ,
- "games" : 0 ,
- "with_win" : 0 ,
- "with_games" : 0 ,
- "against_win" : 0 ,
- "against_games" : 0 ,
- "with_gpm_sum" : 0 ,
- "with_xpm_sum" : 0 ,
- "personaname" : "420 booty wizard" ,
- "name" : "string" ,
- "is_contributor" : true ,
- "is_subscriber" : true ,
- "last_login" : "string" ,
- "avatar" : "string" ,
- "avatarfull" : "string"

## GET /players/{account_id}/pros

Pro players played with
Steam32 account ID
Number of matches to limit to
Number of matches to offset start by
Whether the player won
Patch ID, from dotaconstants
Game Mode ID
Lobby type ID
Region ID
Days previous
Lane Role ID
Hero ID
Whether the player was radiant
Account IDs in the match (array)
Account IDs not in the match (array)
Hero IDs on the player's team (array)
Hero IDs against the player's team (array)
Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches.
The minimum number of games played, for filtering hero stats
The field to return matches sorted by in descending order

### Responses

### Response samples

- 200
- { "account_id" : 0 , "name" : "string" , "country_code" : "string" , "fantasy_role" : 0 , "team_id" : 0 , "team_name" : "Newbee" , "team_tag" : "string" , "is_locked" : true , "is_pro" : true , "locked_until" : 0 , "steamid" : "string" , "avatar" : "string" , "avatarmedium" : "string" , "avatarfull" : "string" , "profileurl" : "string" , "last_login" : "2019-08-24T14:15:22Z" , "full_history_time" : "2019-08-24T14:15:22Z" , "cheese" : 0 , "fh_unavailable" : true , "loccountrycode" : "string" , "last_played" : 0 , "win" : 0 , "games" : 0 , "with_win" : 0 , "with_games" : 0 , "against_win" : 0 , "against_games" : 0 , "with_gpm_sum" : 0 , "with_xpm_sum" : 0 }
- "account_id" : 0 ,
- "name" : "string" ,
- "country_code" : "string" ,
- "fantasy_role" : 0 ,
- "team_id" : 0 ,
- "team_name" : "Newbee" ,
- "team_tag" : "string" ,
- "is_locked" : true ,
- "is_pro" : true ,
- "locked_until" : 0 ,
- "steamid" : "string" ,
- "avatar" : "string" ,
- "avatarmedium" : "string" ,
- "avatarfull" : "string" ,
- "profileurl" : "string" ,
- "last_login" : "2019-08-24T14:15:22Z" ,
- "full_history_time" : "2019-08-24T14:15:22Z" ,
- "cheese" : 0 ,
- "fh_unavailable" : true ,
- "loccountrycode" : "string" ,
- "last_played" : 0 ,
- "win" : 0 ,
- "games" : 0 ,
- "with_win" : 0 ,
- "with_games" : 0 ,
- "against_win" : 0 ,
- "against_games" : 0 ,
- "with_gpm_sum" : 0 ,
- "with_xpm_sum" : 0

## GET /players/{account_id}/totals

Totals in stats
Steam32 account ID
Number of matches to limit to
Number of matches to offset start by
Whether the player won
Patch ID, from dotaconstants
Game Mode ID
Lobby type ID
Region ID
Days previous
Lane Role ID
Hero ID
Whether the player was radiant
Account IDs in the match (array)
Account IDs not in the match (array)
Hero IDs on the player's team (array)
Hero IDs against the player's team (array)
Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches.
The minimum number of games played, for filtering hero stats
The field to return matches sorted by in descending order

### Responses

### Response samples

- 200
- { "field" : "string" , "n" : 0 , "sum" : 0 }
- "field" : "string" ,
- "n" : 0 ,
- "sum" : 0

## GET /players/{account_id}/counts

Counts in categories
Steam32 account ID
Number of matches to limit to
Number of matches to offset start by
Whether the player won
Patch ID, from dotaconstants
Game Mode ID
Lobby type ID
Region ID
Days previous
Lane Role ID
Hero ID
Whether the player was radiant
Account IDs in the match (array)
Account IDs not in the match (array)
Hero IDs on the player's team (array)
Hero IDs against the player's team (array)
Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches.
The minimum number of games played, for filtering hero stats
The field to return matches sorted by in descending order

### Responses

### Response samples

- 200
- "leaver_status" : { } ,
- "game_mode" : { } ,
- "lobby_type" : { } ,
- "lane_role" : { } ,
- "region" : { } ,
- "patch" : { }

## GET /players/{account_id}/histograms

Distribution of matches in a single stat
Steam32 account ID
Field to aggregate on
Number of matches to limit to
Number of matches to offset start by
Whether the player won
Patch ID, from dotaconstants
Game Mode ID
Lobby type ID
Region ID
Days previous
Lane Role ID
Hero ID
Whether the player was radiant
Account IDs in the match (array)
Account IDs not in the match (array)
Hero IDs on the player's team (array)
Hero IDs against the player's team (array)
Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches.
The minimum number of games played, for filtering hero stats
The field to return matches sorted by in descending order

### Responses

### Response samples

- 200
- { }

## GET /players/{account_id}/wardmap

Wards placed in matches played
Steam32 account ID
Number of matches to limit to
Number of matches to offset start by
Whether the player won
Patch ID, from dotaconstants
Game Mode ID
Lobby type ID
Region ID
Days previous
Lane Role ID
Hero ID
Whether the player was radiant
Account IDs in the match (array)
Account IDs not in the match (array)
Hero IDs on the player's team (array)
Hero IDs against the player's team (array)
Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches.
The minimum number of games played, for filtering hero stats
The field to return matches sorted by in descending order

### Responses

### Response samples

- 200
- "obs" : { } ,
- "sen" : { }

## GET /players/{account_id}/wordcloud

Words said/read in matches played
Steam32 account ID
Number of matches to limit to
Number of matches to offset start by
Whether the player won
Patch ID, from dotaconstants
Game Mode ID
Lobby type ID
Region ID
Days previous
Lane Role ID
Hero ID
Whether the player was radiant
Account IDs in the match (array)
Account IDs not in the match (array)
Hero IDs on the player's team (array)
Hero IDs against the player's team (array)
Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches.
The minimum number of games played, for filtering hero stats
The field to return matches sorted by in descending order

### Responses

### Response samples

- 200
- "my_word_counts" : { } ,
- "all_word_counts" : { }

## GET /players/{account_id}/ratings

Returns a history of the player rank tier/medal changes (replaces MMR)
Steam32 account ID

### Responses

### Response samples

- 200
- { "account_id" : 0 , "match_id" : 3703866531 , "solo_competitive_rank" : 0 , "competitive_rank" : 0 , "time" : 0 }
- "account_id" : 0 ,
- "match_id" : 3703866531 ,
- "solo_competitive_rank" : 0 ,
- "competitive_rank" : 0 ,
- "time" : 0

## GET /players/{account_id}/rankings

Player hero rankings
Steam32 account ID

### Responses

### Response samples

- 200
- { "hero_id" : 0 , "score" : 0 , "percent_rank" : 0 , "card" : 0 }
- "hero_id" : 0 ,
- "score" : 0 ,
- "percent_rank" : 0 ,
- "card" : 0

## POST /players/{account_id}/refresh

Refresh player match history (up to 500), medal (rank), and profile name
Steam32 account ID

### Responses

### Response samples

- 200

## top players

## GET /topPlayers

Get list of highly ranked players
Get ratings based on turbo matches

### Responses

### Response samples

- 200
- { "account_id" : 0 , "steamid" : "string" , "avatar" : "string" , "avatarmedium" : "string" , "avatarfull" : "string" , "profileurl" : "string" , "personaname" : "420 booty wizard" , "last_login" : "2019-08-24T14:15:22Z" , "full_history_time" : "2019-08-24T14:15:22Z" , "cheese" : 0 , "fh_unavailable" : true , "loccountrycode" : "string" , "name" : "string" , "country_code" : "string" , "fantasy_role" : 0 , "team_id" : 0 , "team_name" : "Newbee" , "team_tag" : "string" , "is_locked" : true , "is_pro" : true , "locked_until" : 0 , "computed_mmr" : 0 }
- "account_id" : 0 ,
- "steamid" : "string" ,
- "avatar" : "string" ,
- "avatarmedium" : "string" ,
- "avatarfull" : "string" ,
- "profileurl" : "string" ,
- "personaname" : "420 booty wizard" ,
- "last_login" : "2019-08-24T14:15:22Z" ,
- "full_history_time" : "2019-08-24T14:15:22Z" ,
- "cheese" : 0 ,
- "fh_unavailable" : true ,
- "loccountrycode" : "string" ,
- "name" : "string" ,
- "country_code" : "string" ,
- "fantasy_role" : 0 ,
- "team_id" : 0 ,
- "team_name" : "Newbee" ,
- "team_tag" : "string" ,
- "is_locked" : true ,
- "is_pro" : true ,
- "locked_until" : 0 ,
- "computed_mmr" : 0

## pro players

## GET /proPlayers

Get list of pro players

### Responses

### Response samples

- 200
- { "account_id" : 0 , "steamid" : "string" , "avatar" : "string" , "avatarmedium" : "string" , "avatarfull" : "string" , "profileurl" : "string" , "personaname" : "420 booty wizard" , "last_login" : "2019-08-24T14:15:22Z" , "full_history_time" : "2019-08-24T14:15:22Z" , "cheese" : 0 , "fh_unavailable" : true , "loccountrycode" : "string" , "name" : "string" , "country_code" : "string" , "fantasy_role" : 0 , "team_id" : 0 , "team_name" : "Newbee" , "team_tag" : "string" , "is_locked" : true , "is_pro" : true , "locked_until" : 0 , "computed_mmr" : 0 }
- "account_id" : 0 ,
- "steamid" : "string" ,
- "avatar" : "string" ,
- "avatarmedium" : "string" ,
- "avatarfull" : "string" ,
- "profileurl" : "string" ,
- "personaname" : "420 booty wizard" ,
- "last_login" : "2019-08-24T14:15:22Z" ,
- "full_history_time" : "2019-08-24T14:15:22Z" ,
- "cheese" : 0 ,
- "fh_unavailable" : true ,
- "loccountrycode" : "string" ,
- "name" : "string" ,
- "country_code" : "string" ,
- "fantasy_role" : 0 ,
- "team_id" : 0 ,
- "team_name" : "Newbee" ,
- "team_tag" : "string" ,
- "is_locked" : true ,
- "is_pro" : true ,
- "locked_until" : 0 ,
- "computed_mmr" : 0

## pro matches

## GET /proMatches

Get list of pro matches
Get matches with a match ID lower than this value

### Responses

### Response samples

- 200
- { "match_id" : 3703866531 , "duration" : 0 , "start_time" : 0 , "radiant_team_id" : 0 , "radiant_name" : "string" , "dire_team_id" : 0 , "dire_name" : "string" , "leagueid" : 0 , "league_name" : "string" , "series_id" : 0 , "series_type" : 0 , "radiant_score" : 0 , "dire_score" : 0 , "radiant_win" : true , "radiant" : true }
- "match_id" : 3703866531 ,
- "duration" : 0 ,
- "start_time" : 0 ,
- "radiant_team_id" : 0 ,
- "radiant_name" : "string" ,
- "dire_team_id" : 0 ,
- "dire_name" : "string" ,
- "leagueid" : 0 ,
- "league_name" : "string" ,
- "series_id" : 0 ,
- "series_type" : 0 ,
- "radiant_score" : 0 ,
- "dire_score" : 0 ,
- "radiant_win" : true ,
- "radiant" : true

## public matches

## GET /publicMatches

Get list of randomly sampled public matches
Get matches with a match ID lower than this value
Minimum rank for the matches. Ranks are represented by integers (10-15: Herald, 20-25: Guardian, 30-35: Crusader, 40-45: Archon, 50-55: Legend, 60-65: Ancient, 70-75: Divine, 80: Immortal). Each increment represents an additional star.
Maximum rank for the matches. Ranks are represented by integers (10-15: Herald, 20-25: Guardian, 30-35: Crusader, 40-45: Archon, 50-55: Legend, 60-65: Ancient, 70-75: Divine, 80: Immortal). Each increment represents an additional star.

### Responses

### Response samples

- 200
- { "match_id" : 3703866531 , "match_seq_num" : 0 , "radiant_win" : true , "start_time" : 0 , "duration" : 0 , "lobby_type" : 0 , "game_mode" : 0 , "avg_rank_tier" : 0 , "num_rank_tier" : 0 , "cluster" : 0 , "radiant_team" : [ 0 ] , "dire_team" : [ 0 ] }
- "match_id" : 3703866531 ,
- "match_seq_num" : 0 ,
- "radiant_win" : true ,
- "start_time" : 0 ,
- "duration" : 0 ,
- "lobby_type" : 0 ,
- "game_mode" : 0 ,
- "avg_rank_tier" : 0 ,
- "num_rank_tier" : 0 ,
- "cluster" : 0 ,
- "radiant_team" : [ 0 ] ,
- "dire_team" : [ 0 ]

## parsed matches

## GET /parsedMatches

Get list of parsed match IDs
Get matches with a match ID lower than this value

### Responses

### Response samples

- 200
- { "match_id" : 3703866531 }
- "match_id" : 3703866531

## explorer

## GET /explorer

Submit arbitrary SQL queries to the database
The PostgreSQL query as percent-encoded string.

### Responses

### Response samples

- 200

## metadata

## GET /metadata

Site metadata

### Responses

### Response samples

- 200
- "banner" : { }

## distributions

## GET /distributions

Distributions of MMR data by bracket and country

### Responses

### Response samples

- 200
- "ranks" : { "rows" : [ { "bin" : 0 , "bin_name" : 0 , "count" : 0 , "cumulative_sum" : 0 } ] , "sum" : { "count" : 0 } }
- "rows" : [ { "bin" : 0 , "bin_name" : 0 , "count" : 0 , "cumulative_sum" : 0 } ] ,
- { "bin" : 0 , "bin_name" : 0 , "count" : 0 , "cumulative_sum" : 0 }
- "bin" : 0 ,
- "bin_name" : 0 ,
- "count" : 0 ,
- "cumulative_sum" : 0
- "sum" : { "count" : 0 }
- "count" : 0

## search

## GET /search

Search players by personaname.
Search string

### Responses

### Response samples

- 200
- { "account_id" : 0 , "avatarfull" : "string" , "personaname" : "420 booty wizard" , "last_match_time" : "string" , "similarity" : 0 }
- "account_id" : 0 ,
- "avatarfull" : "string" ,
- "personaname" : "420 booty wizard" ,
- "last_match_time" : "string" ,
- "similarity" : 0

## rankings

## GET /rankings

Top players by hero
Hero ID

### Responses

### Response samples

- 200
- "hero_id" : 0 ,
- "rankings" : [ { "account_id" : 0 , "score" : 0 , "steamid" : "string" , "avatar" : "string" , "avatarmedium" : "string" , "avatarfull" : "string" , "profileurl" : "string" , "personaname" : "420 booty wizard" , "last_login" : "2019-08-24T14:15:22Z" , "full_history_time" : "2019-08-24T14:15:22Z" , "cheese" : 0 , "fh_unavailable" : true , "loccountrycode" : "string" , "rank_tier" : 0 } ]
- { "account_id" : 0 , "score" : 0 , "steamid" : "string" , "avatar" : "string" , "avatarmedium" : "string" , "avatarfull" : "string" , "profileurl" : "string" , "personaname" : "420 booty wizard" , "last_login" : "2019-08-24T14:15:22Z" , "full_history_time" : "2019-08-24T14:15:22Z" , "cheese" : 0 , "fh_unavailable" : true , "loccountrycode" : "string" , "rank_tier" : 0 }
- "account_id" : 0 ,
- "score" : 0 ,
- "steamid" : "string" ,
- "avatar" : "string" ,
- "avatarmedium" : "string" ,
- "avatarfull" : "string" ,
- "profileurl" : "string" ,
- "personaname" : "420 booty wizard" ,
- "last_login" : "2019-08-24T14:15:22Z" ,
- "full_history_time" : "2019-08-24T14:15:22Z" ,
- "cheese" : 0 ,
- "fh_unavailable" : true ,
- "loccountrycode" : "string" ,
- "rank_tier" : 0

## benchmarks

## GET /benchmarks

Benchmarks of average stat values for a hero
Hero ID

### Responses

### Response samples

- 200
- "hero_id" : 0 ,
- "result" : { "gold_per_min" : [ { "percentile" : 0 , "value" : 0 } ] , "xp_per_min" : [ { "percentile" : 0 , "value" : 0 } ] , "kills_per_min" : [ { "percentile" : 0 , "value" : 0 } ] , "last_hits_per_min" : [ { "percentile" : 0 , "value" : 0 } ] , "hero_damage_per_min" : [ { "percentile" : 0 , "value" : 0 } ] , "hero_healing_per_min" : [ { "percentile" : 0 , "value" : 0 } ] , "tower_damage" : [ { "percentile" : 0 , "value" : 0 } ] }
- "gold_per_min" : [ { "percentile" : 0 , "value" : 0 } ] ,
- { "percentile" : 0 , "value" : 0 }
- "percentile" : 0 ,
- "value" : 0
- "xp_per_min" : [ { "percentile" : 0 , "value" : 0 } ] ,
- { "percentile" : 0 , "value" : 0 }
- "percentile" : 0 ,
- "value" : 0
- "kills_per_min" : [ { "percentile" : 0 , "value" : 0 } ] ,
- { "percentile" : 0 , "value" : 0 }
- "percentile" : 0 ,
- "value" : 0
- "last_hits_per_min" : [ { "percentile" : 0 , "value" : 0 } ] ,
- { "percentile" : 0 , "value" : 0 }
- "percentile" : 0 ,
- "value" : 0
- "hero_damage_per_min" : [ { "percentile" : 0 , "value" : 0 } ] ,
- { "percentile" : 0 , "value" : 0 }
- "percentile" : 0 ,
- "value" : 0
- "hero_healing_per_min" : [ { "percentile" : 0 , "value" : 0 } ] ,
- { "percentile" : 0 , "value" : 0 }
- "percentile" : 0 ,
- "value" : 0
- "tower_damage" : [ { "percentile" : 0 , "value" : 0 } ]
- { "percentile" : 0 , "value" : 0 }
- "percentile" : 0 ,
- "value" : 0

## health

## GET /health

Get service health data

### Responses

### Response samples

- 200

## request

## GET /request/{jobId}

Get parse request state
The job ID to query.

### Responses

### Response samples

- 200

## POST /request/{match_id}

Submit a new parse request. This call counts as 10 calls for rate limit (but not billing) purposes.

### Responses

### Response samples

- 200

## findMatches

## GET /

Finds recent matches by heroes played
Hero IDs on first team (array)
Hero IDs on second team (array)

### Responses

### Response samples

- 200
- { }

## heroes

## GET /heroes

Get hero data

### Responses

### Response samples

- 200
- { "id" : 0 , "name" : "npc_dota_hero_antimage" , "localized_name" : "Anti-Mage" , "primary_attr" : "string" , "attack_type" : "string" , "roles" : [ "string" ] }
- "id" : 0 ,
- "name" : "npc_dota_hero_antimage" ,
- "localized_name" : "Anti-Mage" ,
- "primary_attr" : "string" ,
- "attack_type" : "string" ,
- "roles" : [ "string" ]
- "string"

## GET /heroes/{hero_id}/matches

Get recent matches with a hero
Hero ID

### Responses

### Response samples

- 200
- { "match_id" : 3703866531 , "duration" : 0 , "start_time" : 0 , "radiant_team_id" : 0 , "radiant_name" : "string" , "dire_team_id" : 0 , "dire_name" : "string" , "leagueid" : 0 , "league_name" : "string" , "series_id" : 0 , "series_type" : 0 , "radiant_score" : 0 , "dire_score" : 0 , "radiant_win" : true , "radiant" : true }
- "match_id" : 3703866531 ,
- "duration" : 0 ,
- "start_time" : 0 ,
- "radiant_team_id" : 0 ,
- "radiant_name" : "string" ,
- "dire_team_id" : 0 ,
- "dire_name" : "string" ,
- "leagueid" : 0 ,
- "league_name" : "string" ,
- "series_id" : 0 ,
- "series_type" : 0 ,
- "radiant_score" : 0 ,
- "dire_score" : 0 ,
- "radiant_win" : true ,
- "radiant" : true

## GET /heroes/{hero_id}/matchups

Get results against other heroes for a hero
Hero ID

### Responses

### Response samples

- 200
- { "hero_id" : 0 , "games_played" : 0 , "wins" : 0 }
- "hero_id" : 0 ,
- "games_played" : 0 ,
- "wins" : 0

## GET /heroes/{hero_id}/durations

Get hero performance over a range of match durations
Hero ID

### Responses

### Response samples

- 200
- { "duration_bin" : "string" , "games_played" : 0 , "wins" : 0 }
- "duration_bin" : "string" ,
- "games_played" : 0 ,
- "wins" : 0

## GET /heroes/{hero_id}/players

Get players who have played this hero
Hero ID

### Responses

### Response samples

- 200
- [ { "account_id" : 0 , "steamid" : "string" , "avatar" : "string" , "avatarmedium" : "string" , "avatarfull" : "string" , "profileurl" : "string" , "personaname" : "420 booty wizard" , "last_login" : "2019-08-24T14:15:22Z" , "full_history_time" : "2019-08-24T14:15:22Z" , "cheese" : 0 , "fh_unavailable" : true , "loccountrycode" : "string" , "name" : "string" , "country_code" : "string" , "fantasy_role" : 0 , "team_id" : 0 , "team_name" : "Newbee" , "team_tag" : "string" , "is_locked" : true , "is_pro" : true , "locked_until" : 0 , "computed_mmr" : 0 } ]
- { "account_id" : 0 , "steamid" : "string" , "avatar" : "string" , "avatarmedium" : "string" , "avatarfull" : "string" , "profileurl" : "string" , "personaname" : "420 booty wizard" , "last_login" : "2019-08-24T14:15:22Z" , "full_history_time" : "2019-08-24T14:15:22Z" , "cheese" : 0 , "fh_unavailable" : true , "loccountrycode" : "string" , "name" : "string" , "country_code" : "string" , "fantasy_role" : 0 , "team_id" : 0 , "team_name" : "Newbee" , "team_tag" : "string" , "is_locked" : true , "is_pro" : true , "locked_until" : 0 , "computed_mmr" : 0 }
- "account_id" : 0 ,
- "steamid" : "string" ,
- "avatar" : "string" ,
- "avatarmedium" : "string" ,
- "avatarfull" : "string" ,
- "profileurl" : "string" ,
- "personaname" : "420 booty wizard" ,
- "last_login" : "2019-08-24T14:15:22Z" ,
- "full_history_time" : "2019-08-24T14:15:22Z" ,
- "cheese" : 0 ,
- "fh_unavailable" : true ,
- "loccountrycode" : "string" ,
- "name" : "string" ,
- "country_code" : "string" ,
- "fantasy_role" : 0 ,
- "team_id" : 0 ,
- "team_name" : "Newbee" ,
- "team_tag" : "string" ,
- "is_locked" : true ,
- "is_pro" : true ,
- "locked_until" : 0 ,
- "computed_mmr" : 0

## GET /heroes/{hero_id}/itemPopularity

Get item popularity of hero categoried by start, early, mid and late game, analyzed from professional games
Hero ID

### Responses

### Response samples

- 200
- "start_game_items" : { "item" : 0 } ,
- "item" : 0
- "early_game_items" : { "item" : 0 } ,
- "item" : 0
- "mid_game_items" : { "item" : 0 } ,
- "item" : 0
- "late_game_items" : { "item" : 0 }
- "item" : 0

## hero stats

## GET /heroStats

Get stats about hero performance in recent matches

### Responses

### Response samples

- 200
- { "id" : 0 , "name" : "npc_dota_hero_antimage" , "localized_name" : "Anti-Mage" , "primary_attr" : "string" , "attack_type" : "string" , "roles" : [ "string" ] , "img" : "string" , "icon" : "string" , "base_health" : 0 , "base_health_regen" : 0 , "base_mana" : 0 , "base_mana_regen" : 0 , "base_armor" : 0 , "base_mr" : 0 , "base_attack_min" : 0 , "base_attack_max" : 0 , "base_str" : 0 , "base_agi" : 0 , "base_int" : 0 , "str_gain" : 0 , "agi_gain" : 0 , "int_gain" : 0 , "attack_range" : 0 , "projectile_speed" : 0 , "attack_rate" : 0 , "base_attack_time" : 0 , "attack_point" : 0 , "move_speed" : 0 , "turn_rate" : 0 , "cm_enabled" : true , "legs" : 0 , "day_vision" : 0 , "night_vision" : 0 , "hero_id" : 0 , "turbo_picks" : 0 , "turbo_wins" : 0 , "pro_ban" : 0 , "pro_win" : 0 , "pro_pick" : 0 , "1_pick" : 0 , "1_win" : 0 , "2_pick" : 0 , "2_win" : 0 , "3_pick" : 0 , "3_win" : 0 , "4_pick" : 0 , "4_win" : 0 , "5_pick" : 0 , "5_win" : 0 , "6_pick" : 0 , "6_win" : 0 , "7_pick" : 0 , "7_win" : 0 , "8_pick" : 0 , "8_win" : 0 }
- "id" : 0 ,
- "name" : "npc_dota_hero_antimage" ,
- "localized_name" : "Anti-Mage" ,
- "primary_attr" : "string" ,
- "attack_type" : "string" ,
- "roles" : [ "string" ] ,
- "string"
- "img" : "string" ,
- "icon" : "string" ,
- "base_health" : 0 ,
- "base_health_regen" : 0 ,
- "base_mana" : 0 ,
- "base_mana_regen" : 0 ,
- "base_armor" : 0 ,
- "base_mr" : 0 ,
- "base_attack_min" : 0 ,
- "base_attack_max" : 0 ,
- "base_str" : 0 ,
- "base_agi" : 0 ,
- "base_int" : 0 ,
- "str_gain" : 0 ,
- "agi_gain" : 0 ,
- "int_gain" : 0 ,
- "attack_range" : 0 ,
- "projectile_speed" : 0 ,
- "attack_rate" : 0 ,
- "base_attack_time" : 0 ,
- "attack_point" : 0 ,
- "move_speed" : 0 ,
- "turn_rate" : 0 ,
- "cm_enabled" : true ,
- "legs" : 0 ,
- "day_vision" : 0 ,
- "night_vision" : 0 ,
- "hero_id" : 0 ,
- "turbo_picks" : 0 ,
- "turbo_wins" : 0 ,
- "pro_ban" : 0 ,
- "pro_win" : 0 ,
- "pro_pick" : 0 ,
- "1_pick" : 0 ,
- "1_win" : 0 ,
- "2_pick" : 0 ,
- "2_win" : 0 ,
- "3_pick" : 0 ,
- "3_win" : 0 ,
- "4_pick" : 0 ,
- "4_win" : 0 ,
- "5_pick" : 0 ,
- "5_win" : 0 ,
- "6_pick" : 0 ,
- "6_win" : 0 ,
- "7_pick" : 0 ,
- "7_win" : 0 ,
- "8_pick" : 0 ,
- "8_win" : 0

## leagues

## GET /leagues

Get league data

### Responses

### Response samples

- 200
- { "leagueid" : 0 , "ticket" : "string" , "banner" : "string" , "tier" : "string" , "name" : "ASUS ROG DreamLeague Season 4" }
- "leagueid" : 0 ,
- "ticket" : "string" ,
- "banner" : "string" ,
- "tier" : "string" ,
- "name" : "ASUS ROG DreamLeague Season 4"

## GET /leagues/{league_id}

Get data for a league
League ID

### Responses

### Response samples

- 200
- { "leagueid" : 0 , "ticket" : "string" , "banner" : "string" , "tier" : "string" , "name" : "ASUS ROG DreamLeague Season 4" }
- "leagueid" : 0 ,
- "ticket" : "string" ,
- "banner" : "string" ,
- "tier" : "string" ,
- "name" : "ASUS ROG DreamLeague Season 4"

## GET /leagues/{league_id}/matches

Get matches for a league (excluding amateur leagues)
League ID

### Responses

### Response samples

- 200
- "match_id" : 3703866531 ,
- "duration" : 0 ,
- "start_time" : 0 ,
- "radiant_team_id" : 0 ,
- "radiant_name" : "string" ,
- "dire_team_id" : 0 ,
- "dire_name" : "string" ,
- "leagueid" : 0 ,
- "league_name" : "string" ,
- "series_id" : 0 ,
- "series_type" : 0 ,
- "radiant_score" : 0 ,
- "dire_score" : 0 ,
- "radiant_win" : true ,
- "radiant" : true

## GET /leagues/{league_id}/matchIds

Get match IDs for a league (including amateur leagues)
League ID

### Responses

### Response samples

- 200
- "string"

## GET /leagues/{league_id}/teams

Get teams for a league
League ID

### Responses

### Response samples

- 200
- "team_id" : 0 ,
- "rating" : 0 ,
- "wins" : 0 ,
- "losses" : 0 ,
- "last_match_time" : 0 ,
- "name" : "Newbee" ,
- "tag" : "string"

## teams

## GET /teams

Get team data
Page number, zero indexed. Each page returns up to 1000 entries.

### Responses

### Response samples

- 200
- { "team_id" : 0 , "rating" : 0 , "wins" : 0 , "losses" : 0 , "last_match_time" : 0 , "name" : "Newbee" , "tag" : "string" }
- "team_id" : 0 ,
- "rating" : 0 ,
- "wins" : 0 ,
- "losses" : 0 ,
- "last_match_time" : 0 ,
- "name" : "Newbee" ,
- "tag" : "string"

## GET /teams/{team_id}

Get data for a team
Team ID

### Responses

### Response samples

- 200
- "team_id" : 0 ,
- "rating" : 0 ,
- "wins" : 0 ,
- "losses" : 0 ,
- "last_match_time" : 0 ,
- "name" : "Newbee" ,
- "tag" : "string"

## GET /teams/{team_id}/matches

Get matches for a team
Team ID

### Responses

### Response samples

- 200
- "match_id" : 3703866531 ,
- "radiant" : true ,
- "radiant_win" : true ,
- "radiant_score" : 0 ,
- "dire_score" : 0 ,
- "duration" : 0 ,
- "start_time" : 0 ,
- "leagueid" : 0 ,
- "league_name" : "string" ,
- "cluster" : 0 ,
- "opposing_team_id" : 0 ,
- "opposing_team_name" : "string" ,
- "opposing_team_logo" : "string"

## GET /teams/{team_id}/players

Get players who have played for a team
Team ID

### Responses

### Response samples

- 200
- "account_id" : 0 ,
- "name" : "string" ,
- "games_played" : 0 ,
- "wins" : 0 ,
- "is_current_team_member" : true

## GET /teams/{team_id}/heroes

Get heroes for a team
Team ID

### Responses

### Response samples

- 200
- "hero_id" : 0 ,
- "name" : "Anti-Mage" ,
- "games_played" : 0 ,
- "wins" : 0

## records

## GET /records/{field}

Get top performances in a stat
Field name to query

### Responses

### Response samples

- 200
- { "match_id" : 3703866531 , "start_time" : 0 , "hero_id" : 0 , "score" : 0 }
- "match_id" : 3703866531 ,
- "start_time" : 0 ,
- "hero_id" : 0 ,
- "score" : 0

## live

## GET /live

Get top currently ongoing live games

### Responses

### Response samples

- 200
- { }

## scenarios

## GET /scenarios/itemTimings

Win rates for certain item timings on a hero for items that cost at least 1400 gold
Filter by item name e.g. "spirit_vessel"
Hero ID

### Responses

### Response samples

- 200
- { "hero_id" : 0 , "item" : "string" , "time" : 0 , "games" : "string" , "wins" : "string" }
- "hero_id" : 0 ,
- "item" : "string" ,
- "time" : 0 ,
- "games" : "string" ,
- "wins" : "string"

## GET /scenarios/laneRoles

Win rates for heroes in certain lane roles
Filter by lane role 1-4 (Safe, Mid, Off, Jungle)
Hero ID

### Responses

### Response samples

- 200
- { "hero_id" : 0 , "lane_role" : 0 , "time" : 0 , "games" : "string" , "wins" : "string" }
- "hero_id" : 0 ,
- "lane_role" : 0 ,
- "time" : 0 ,
- "games" : "string" ,
- "wins" : "string"

## GET /scenarios/misc

Miscellaneous team scenarios
Name of the scenario (see teamScenariosQueryParams)

### Responses

### Response samples

- 200
- { "scenario" : "string" , "is_radiant" : true , "region" : 0 , "games" : "string" , "wins" : "string" }
- "scenario" : "string" ,
- "is_radiant" : true ,
- "region" : 0 ,
- "games" : "string" ,
- "wins" : "string"

## schema

## GET /schema

Get database schema

### Responses

### Response samples

- 200
- { "table_name" : "string" , "column_name" : "string" , "data_type" : "string" }
- "table_name" : "string" ,
- "column_name" : "string" ,
- "data_type" : "string"

## constants

## GET /constants

Get static game data mirrored from the dotaconstants repository.
Resource name e.g. heroes . List of resources
[LINK: List of resources](https://github.com/odota/dotaconstants/tree/master/build)

### Responses

### Response samples

- 200

--------------------