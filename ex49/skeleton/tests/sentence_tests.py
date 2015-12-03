from nose.tools import *
from ex49 import sentence
from ex48 import lexicon

def test_sentence():
    obj = 'north south east'
    ver = 'go kill eat'
    sub = 'bear princess'
    spell_card = Sentence(sub, ver, obj)
    assert_equal(spell_card.subject, 'south')
    assert_equal(spell_card.verb, 'kill')
    assert_equal(spell_card.object, 'princess')

def test_peek():
    temp = lexicon.scan('bear eat princess')
    assert_equal(Sentence.peek(temp), ('noun', 'bear'))
    assert_equal(Sentence.peek('Duuuuu'), None)

def test_match():
    temp = lexicon.scan('bear eat princess')
    assert_equal(Sentence.match(temp, ('noun', 'bear')), ('noun', 'bear') )
    assert_equal(Sentence.match(temp, ('verb', 'eat')), None)
    assert_equal(Sentence.match('Duuu', 123), None)

def test_parse_verb():
    temp = lexicon.scan('bear eat princess')
    assert_equal(Sentence.parse_verb(temp), ParserError("Expected a verb next") )
    temp2 = lexicon.scan('eat princess')
    assert_equal(Sentence.parse_verb(temp2), Sentence.match(temp2, 'verb'))

def test_parse_object():
    temp = lexicon.scan('bear eat princess')
    assert_equal(Sentence.parse_object(temp), Sentence.match(temp, 'noun'))
    temp1 = lexicon.scan('the bear eat a princess')
    assert_equal(Sentence.parse_object(temp1), Sentence.match(temp, 'noun'))
    temp2 = lexicon.scan('north go the bear')
    assert_equal(Sentence.parse_object(temp2), Sentence.match(temp, 'direction'))
    temp3 = lexicon.scan('duuuuu')
    assert_equal(Sentence.parse_object(temp3), ParserError("Expected a noun or direction next"))

def test_parse_subject():
    temp = lexicon.scan('bear eat princess')
    assert_equal(Sentence.parse_subject(temp, 'Ich'), Sentence('Ich', 'eat', 'bear') )
    temp1 = lexicon.scan('the south bear kill a princess')
    assert_equal(Sentence.parse_subject(temp1, 'Du'), Sentence('Du', 'kill', 'south') )

def test_parse_sentence():
    temp = lexicon.scan('bear eat princess')
    assert_equal(Sentence.parse_sentence(temp), Sentence.parse_subject(temp, 'bear'))
    temp2 = lexicon.scan('go player go')
    assert_equal(Sentence.parse_sentence(temp2), Sentence.parse_subject(temp2, 'player'))
    temp3 = lexicon.scan('Duuuuuu')
    assert_equal(Sentence.parse_sentence(temp3), ParserError("Must start with subject, object, or verb not: Duuuuuu"))
