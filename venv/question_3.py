Jordan_belfort = {'samtaler': 178, 'møter': 17, 'salg': 6}

call_point = 10
meeting_point = 30
sale_point = 100

bonus_point = 100



def score_cal():
    call_points = 10 * Jordan_belfort.get('samtaler')
    meeting_points = 30 * Jordan_belfort.get('møter')
    sale_points = 178 * Jordan_belfort.get('salg')


    if Jordan_belfort.get('samtaler')>=150:
        sum_points = call_points + meeting_points + sale_points + bonus_point
        Jordan_belfort['score'] = sum_points
        print(Jordan_belfort)
        if Jordan_belfort.get('samtaler')>=300:
            sum_points = call_points + meeting_points + sale_points + bonus_point*2
            Jordan_belfort['score'] = sum_points
            print(Jordan_belfort)
        elif Jordan_belfort.get('samtaler')>=450:
            sum_points = call_points + meeting_points + sale_points + bonus_point * 3
            Jordan_belfort['score'] = sum_points
            print(Jordan_belfort)
    else:
        sum_points = call_points + meeting_points + sale_points
        Jordan_belfort['score'] = sum_points
        print(Jordan_belfort)

score_cal()