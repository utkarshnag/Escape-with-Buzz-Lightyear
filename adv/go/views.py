from django.shortcuts import render
from django.views.generic import TemplateView
from .eng import *

# Create your views here.
class HomePageView(TemplateView):

    play = []
    play.append(start)
    seq = []
    seq.append(play[0].description)

    def get(self, request, **kwargs):
        seq = []
        seq.append(start.description)
        story = {
            'sequence': seq
        }
        return render(request, 'index.html', story)
    
    def post(self, request, **kwargs):
        text = request.POST.get('cmd')
        words = text.split() 
        self.seq.append('>>>'+text)
        play = self.play[-1]
        done = 0
        
        if (text == 'go' or text == 'Go'):
            self.seq.append("Go where?")
            done = 1            

        for word in words:       
            if (word in play.paths):
                play = play.go(word)
                self.seq.append(play.description)
                self.play.append(play)
                done = 1
                break

        if (text == 'try again' or text == 'restart'):
            done = 1
            self.play.append(start)
            self.seq.append(self.play[0].description)
                
        if (done == 0):
            self.seq.append("Try something else or be more specific.")
                
        story = {
            'sequence': self.seq
        }
        
        return render(request, 'index.html', story)
        
