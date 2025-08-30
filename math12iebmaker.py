from abstractrectanglemaker import AbstractRectangleMaker

class Math12IEBMaker(AbstractRectangleMaker):
    def regex_separators(self):
        patterns={
            "main_questions":r"(QUESTION \d+\s+[\s\S]+?)(?=\nQUESTION \d+|\Z)",
            "sub_questions": r"(\([a-z0-9]\)\s.*[\s\S]+?)((?=^\([a-hj-z]\)|^(NATIONAL)|\Z))",
            "subsub_questions":r"(?<=\([0-9]\))(\s{3,}|$)",
            "memo_start_keys":r"\s\n"


        }