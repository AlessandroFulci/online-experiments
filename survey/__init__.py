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
  input_button6 = models.CharField(
      choices=[["1", '1 - Short-term economic benefits are much more important than potential long-term environmental consequences'],
            ["2", '2 - Short-term economic benefits are somewhat more important than potential long-term environmental consequences'],
            ["3", '3 - Short-term economic benefits and potential long-term environmental consequences are equally important'],
            ["4", '4 - Potential long-term environmental consequences are somewhat more important than short-term economic benefits'],
            ["5", '5 - Potential long-term environmental consequences are much more important than short-term economic benefits']],
    widget=widgets.RadioSelect,
    label="7- On a scale of 1-5, how much weight would you give to the potential long-term environmental consequences of allowing companies to pollute the Stelvio National Park, compared to the short-term economic benefits? ")
  input_button7 = models.CurrencyField()
  input_button8 = models.CharField(
      choices=[
            ["1", 'You can’t afford any extra expenditure? '],
            ["2", 'You think biodiversity should be protected by law, and we shouldn’t have to individually pay money to protect it? '],
            ["3", 'You don’t believe that environmental quality protection is important at all?'],
            ["4", 'You don’t believe that environmental quality protection is important in this example?'],
            ["5", 'Other reasons'],
            ["6", 'I previously aswered that I would pay a positive amount']],
    widget=widgets.RadioSelect,
    label="9- If you have said that you would not be willing to pay anything, is this because:")
  input_button9 = models.CharField(
      choices=[
            ["1", 'Yes'],
            ["2", 'No']],
    widget=widgets.RadioSelect,
    label="10- Do you believe that environmental problems are of serious concern today?")
  input_button10 = models.CharField(
      choices=[
            ["1", 'lower than 8.000€'],
            ["2", '8.000-15.000€'],
            ["3", '15.000-28.000€'],
            ["4", '28.000-50.000€'],
            ["5", 'higher than 50.000€']],
    widget=widgets.RadioSelect,
    label="11- Is the gross (Before tax, etc.) annual income of your household:")
  input_dropdown = models.StringField(
       choices=['Male','Female','Other'])      
  input_dropdown2 = models.StringField(
       choices=['Highschool','Bachelor Degree','Master Degree','PhD']) 
  input_buttonAGE = models.IntegerField()
def creating_session(subsession):
    for g in subsession.get_groups():
        for p in g.get_players():
            if p.id_in_group % 3 == 0:
                p.treatment="Baseline"
            if p.id_in_group % 3 == 1:
                p.treatment="Treatment1"
            if p.id_in_group % 3 == 2:
                p.treatment="Treatment2" 

# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['input_checker','input_button','input_button2','input_button3','input_button4','input_button5','input_button6','input_button7']

class MyPage2(Page):
    form_model = 'player'
    form_fields = ['input_button8','input_button9','input_button10','input_dropdown','input_dropdown2','input_buttonAGE']

class BaselineT(Page):
  @staticmethod
#   def vars_for_template(player: Player):
#     return dict(
#     treatment = player.treatment)
  def is_displayed(player: Player):
      return player.treatment == "Baseline"
  
class Display(Page):
    @staticmethod
    # def vars_for_template(player: Player):
    #     return dict(
    #         treatment = player.treatment
    #     )
    def is_displayed(player: Player):
      return player.treatment == "Treatment1"

class YT(Page):
  @staticmethod
#   def vars_for_template(player: Player):
#     return dict(
#     treatment = player.treatment)
  def is_displayed(player: Player):
      return player.treatment == "Treatment2"
  
class Donation(Page):
   pass


class ResultsWaitPage(WaitPage):
    pass

class Results(Page):
    pass


page_sequence = [BaselineT,Display,YT,MyPage,Donation,MyPage2,Results]
