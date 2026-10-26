# Issues:

## Major

## Minor

## Minuscule

# Fixed:

### Importing starships as one object 
- All 36 ships imported under one object.

#### Fix:
- Redoing my import to convert the data to a python list once exported from JSON, and upon importing I drop the table untill it imports all 36, this was a quick fix as otherwise, my first import brought in duplicated ships, with ~96 individual objects.

### Getting pilots from database and adding id to star ships
- Reason:
The reason for this being an issue, is due to the characters from the current dataset, in my database are using old data, I will need to re-import the new version of characters, as to match how starships was created.

#### Fix:
- Imported the new version of the people/characters data. Filtered by characters with ships, and then add their id from the database, to the starships collection pilots column.