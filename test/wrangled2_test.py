


from my_lambdata.assignment1 import WrangledFrame
    
def test_add_state_names():
    wf = WrangledFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    #self.assertEqual(list(wf.columns), ['abbrev'])
    #self.assertEqual(len(list(wf.columns)), 1)
    assert list(wf.columns) == ["abbrev"]

    wf.add_state_names()
    #ensure there is a "name" column
    #self.assertEqual(list(wf.columns), ['abbrev', 'name'])
    #self.assertEqual(len(list(wf.columns)), 2)
    assert list(wf.columns) == ["abbrev", "name"]

    #ensure the values of Wf are specific classes/ values (string, "California")
    #self.assertEqual(wf["name"][0], 'Cali')
    assert wf["name"][0] == "Cali"
    assert wf["abbrev"][0] == "CA"

    #self.assertEqual(wf['abbrev'][0], "CA")
      