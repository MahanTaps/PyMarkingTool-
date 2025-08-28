from abc import ABC, abstractmethod
from pathlib import Path

class AbstractRectangleMaker(ABC):
    @property
    @abstractmethod
    def regex_separators(self):
        """Creates a dict of all the q and a separators"""
        pass 

    @property
    @abstractmethod
    def question_rectangles(self,document):
        """Creates a list of all the question rectangles with their page numbers"""
        pass 
    @property
    @abstractmethod
    def answer_rectangles(self,memo):
        """Creates a list of all the answer rectangles with their page numbers"""
        pass 

    @property
    @abstractmethod 
    def question_titles(self,document):
        """Creates a list of The titles to each question"""
        pass 

    @property 
    @abstractmethod 
    def question_stem_rectangles(self,document):
        """Creates a list of The stems for each question if there are any"""
        pass 

    @property 
    @abstractmethod 
    def mark_allocations(self,document):
        """Creates a list of The mark allocations for each question"""
        pass 

#The only thing I need to change is the way the rectangles are made between paper types
#1.) An abstract Rectangle Factory 
#2.) Concrete screenshotter 
#3.) Concrete SQL writer 
#4.) Concrete SQL model
#5.) Concrete AI API accessor 
#6.) A concrete Rectangle maker