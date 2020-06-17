"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# work in progress, need to add logic to allow user to choose a story


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

game = Story(
    ['noun', 'verb'],
    """ In the game Star Wars you are Luke Skywalker
    and you try to destroy every {noun}. In
    a car racing/motorcycle racing game you need to beat
    every computerized vehicle that you are
    {verb} against. """
)

school = Story(
    ["adjective", "noun"],
    """In school, I met two really {adjective} kids. All of us became 
    friends very fast. That day we had Science, and
    luckily my friends and I were at the same {noun}"""
)

jungle = Story(
    ["adjective", "noun", "verb"],
    """I walk through the color jungle. I take out my
    {adjective} canteen. There's a {adjective} parrot with a {adjective}
    {noun} in his mouth right there in front of me in the {adjective} trees! I gaze at his 
    {adjective} {noun}. A sudden sound awakes me from my daydream!
    A panther’s {verb} in front of my head! I {verb} his {adjective}
    breath. I remember I have a packet of {noun} that makes go into a deep
    slumber! I {verb} it away from me in front of the {noun}.
    Yes he's eating it! I {verb} away through the {adjective} jungle. 
    I meet my parents at the tent. Phew! 
    It’s been an exciting day in the jungle. """
)

{"stories": story, "stories": game, "stories": school, "stories": jungle}
story_list = {s.stories: s for s in [story, game, school, jungle]}
