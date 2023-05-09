from otree.api import *


doc = """
THIS APP IS MADE TO ASK PEOPLE QUESTIONS ABOUT ENVIROMENT AND EVENTUAL COMPENSATIONS THEY WOULD ACCEPT TO 
ALLOW POLLUTION. 
"""


class C(BaseConstants):
    NAME_IN_URL = 'SURVEY'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
  treatment= models.CharField()
  input_checker = models.CharField(
    choices=[
            ["1", '1 - Not at all important'],
            ["2", '2 - Slightly important'],
            ["3",'3 - Moderately important'],
            ["4",'4 - Very important'],
            ["5","5 - Extremely important"]],
    widget=widgets.RadioSelect,
    label="1- On a scale of 1-5, how important is it to you to protect the environment in the Stelvio National Park?")
  input_button = models.CharField(choices=[
            ["1", 'Yes'],
            ["0", 'No']],
    widget=widgets.RadioSelect,label="")
  input_button2 = models.CharField(
      choices=[
            ["1", '1 - Economic benefits are much more important than environmental consequences'],
            ["2", '2 - Economic benefits are somewhat more important than environmental consequences'],
            ["3", '3 - Economic benefits and environmental consequences are equally'],
            ["4", '4 - Environmental consequences are somewhat more important than economic benefits'],
            ["5", '5 - Environmental consequences are much more important than economic benefits']],
    widget=widgets.RadioSelect,
    label="3- On a scale of 1-5, how much weight would you give to the economic benefits of allowing companies to pollute the Stelvio National Park, compared to the environmental consequences?")
  input_button3 = models.CharField(choices=[
            ["1", 'Yes'],
            ["0", 'No']],
    widget=widgets.RadioSelect,label="4- If it were up to you, would you prioritize economic growth and job creation over environmental protection in the Stelvio National Park?")
  input_button4 = models.CharField(
      choices=[
            ["1", '1 - Strongly disagree'],
            ["2", '2 - Somewhat disagree '],
            ["3", '3 - Neutral'],
            ["4", '4 - Somewhat agree'],
            ["5", '5 - Strongly agree']],
    widget=widgets.RadioSelect,
    label="5- On a scale of 1-5, how strongly do you agree with the following statement: Protecting the environment in the Stelvio National Park should always take precedence over economic considerations.")
  input_button5 = models.CharField(
      choices=[
            ["1", '1 - Economic growth'],
            ["2", '2 - Environmental protection']],
    widget=widgets.RadioSelect,
    label="6- If there were a conflict between local economic growth and environmental protection in the Stelvio National Park, which would you prioritize?")
              

def creating_session(subsession):
    for g in subsession.get_groups():
        for p in g.get_players():
            if p.id_in_group % 2 == 0:
                p.treatment="Baseline"
            if p.id_in_group % 2 == 1:
                p.treatment="Treatment" 

# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['input_checker','input_button','input_button2','input_button3','input_button4','input_button5']

class Display(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            treatment = player.treatment
        )


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Display,MyPage,Results]#ResultsWaitPage, Results]
