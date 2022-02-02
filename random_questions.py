import random

def run():
    work= ('what is your job?','where do you work?','why do you choose that job?','is it a popular job in your country?','do you like your job?','do you get on well with your colleagues?','what was your first day like?','what responsabilities do you have at work?','if you had the chance, would you change your job?','do you plan to continue with your job in the future?')
    study=('what do you study?','where do you study that?','why did you choose that subject?','is it a popular subject in your contry?','do you like that subject?','do you get on with your colleagues?','what was your first day like?','what are the main aspects of your subjects?','if you had the chance, would you change subject?','do you plan to get a job in the same field as your subject?')
    hometown=('where is your hometown?','do you like your hometown?','do you often visit your hometown?','what is there for a foreingner to do or see in your hometown?','how could your hometown be improved?','has your hometown changed much since you were a child?','is there good public transportation in you hometown?','do you think your hometown is a good place to bring up children?')
    topics=(work, study,hometown) #'home','art','birthdays','childhood','clothes','computers','daily_routine','dictionaries','evenings','family/friends','flowers','food','going_out','happiness','hobbies','internet','leisure_time','music','neighbourhood','news_paper','pets','reading','shopping','sport','tv','transport','weather')
    random_topic= random.choice(topics)

    if random_topic==work:       
        the_3_questions=[]

        for x in range(3):
            questions=random.choice(work)
            the_3_questions.append(questions)
        print(the_3_questions)





if __name__=='__main__':
    run()