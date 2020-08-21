Jordan_belfort = {'samtaler': 178, 'møter': 17, 'salg': 6}

call_point = 10
meeting_point = 30
sale_point = 100

bonus_point = 100




call_points = 10 * Jordan_belfort.get('samtaler')
meeting_points = 30 * Jordan_belfort.get('møter')
sale_points = 100 * Jordan_belfort.get('salg')
sum_points = call_points + meeting_points + sale_points + bonus_point

Jordan_belfort['score'] = sum_points
print(Jordan_belfort)