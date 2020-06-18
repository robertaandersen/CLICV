import Navigation as navigate

def prompt_educationList():
    

    print('+-----------------------------------------------------+')
    print('|Main:                                                |')
    print('|    University of Iceland: B.Sc – Computer Science   |')
    print('|    Aug, 2010 - Feb, 2014                            |')
    print('+-----------------------------------------------------+')
    print('|    F.Í.H. School of Music: Diploma in Jazz Guitar   |')
    print('|    Aug, 1998 - Feb, 2003                            |')
    print('+-----------------------------------------------------+')
    print('|    Menntaskóli Akureyrar: Stúdentspróf              |')
    print('|    Aug, 1994 - Jun, 1998                            |')
    print('+-----------------------------------------------------+')
    print()
    print('+-----------------------------------------------------+')
    print('|Other:                                               |')
    print('|    Kungliga musikhögskolan Stockholm - Exchange year|')
    print('|    Aug, 2001 - Jun, 2002                            |')
    print('+-----------------------------------------------------+')
    print('|    Coursera - Devops culture and practices          |')
    print('|    Aug, 2019                                        |')
    print('+-----------------------------------------------------+')
    print('|    Coursera - Google Kubernetes Engine              |')
    print('|    Sept 2019                                        |')
    print('+-----------------------------------------------------+')



    navigate.prompt_back(lambda : navigate.prompt_main_menu())