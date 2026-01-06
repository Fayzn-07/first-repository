moma_artworks = {"Starry Night", "The Persistence of Memory", "The Scream", "Girl with a Pearl Earring"}
louvre_artworks = {"Mona Lisa", "The Scream", "Liberty Leading the People", "Girl with a Pearl Earring"}
rijksmuseum_artworks = {"The Night Watch", "Girl with a Pearl Earring", "The Milkmaid", "Starry Night"} 

moma_artworks.update({"Composition with Red, Blue, Yellow"})
print("\n =>Updated moma_artworks",moma_artworks)

Shared_masterpieces = moma_artworks.intersection(louvre_artworks,rijksmuseum_artworks)
print("\n =>Shared_masterpieces",Shared_masterpieces)

louvre_artworks.update({"Raft of the Medusa", "Liberty Leading the People"})
print("\n =>Updated louvre_artworks",louvre_artworks)

rijksmuseum_artworks.update({"The Jewish Bride","The Milkmaid"})
print("\n =>New items added to rijksmuseum_artworks",rijksmuseum_artworks)

master_list = moma_artworks.union(louvre_artworks,rijksmuseum_artworks)
print("\n =>Master_list:",master_list)

rijksmuseum_artworks.discard("The Milkmaid")
print("\n =>Milkmaid removed from rijksmuseum_artworks",rijksmuseum_artworks)

Momas_Unique_Artworks = moma_artworks.difference(louvre_artworks,rijksmuseum_artworks)
print("\n =>Unique pieces in moma_artworks:",Momas_Unique_Artworks)  


