


# WebScraping_PremierLeagueTable

Exporting Web Table Standings to Excel sheet

Comparing mini-projects like this and an IMDB one, this is a little more complicated.

Let's look a little closer:

### Table headers:
```markdown
```html
<thead>
    <tr class="standing-table__row">
        <th class="standing-table__cell standing-table__header-cell" title="Position" data-label="pos" data-index="0">#</th>
        <th class="standing-table__cell standing-table__header-cell standing-table__cell--name" title="Team" data-index="1">Team</th>
        <th class="standing-table__cell standing-table__header-cell" title="Played" data-label="pld" data-index="2">Pl</th>
        <th class="standing-table__cell standing-table__header-cell is-hidden--bp35" title="Won" data-label="w" data-index="3">W</th>
        <th class="standing-table__cell standing-table__header-cell is-hidden--bp35" data-label="d" data-index="4">D</th>
        <th class="standing-table__cell standing-table__header-cell is-hidden--bp35" data-label="l" data-index="5">L</th>
        <th class="standing-table__cell standing-table__header-cell is-hidden--bp35" data-label="f" data-index="6">F</th>
        <th class="standing-table__cell standing-table__header-cell is-hidden--bp35" data-label="a" data-index="7">A</th>
        <th class="standing-table__cell standing-table__header-cell" data-label="gd" data-index="8">GD</th>
        <th class="standing-table__cell standing-table__header-cell" data-label="pts" data-sort-value="use-attribute" data-index="9">Pts</th>
        <th class="standing-table__cell standing-table__header-cell is-hidden--bp15 is-hidden--bp35 " data-sort-value="use-attribute" data-index="10">Last 6</th>
    </tr>
</thead>
```

### Content example:

```html
<tr class="standing-table__row" data-item-id="345">
    <td class="standing-table__cell">1</td>
    <td class="standing-table__cell standing-table__cell--name" data-short-name="Manchester City" data-long-name="Manchester City">
        <a href="/manchester-city" class="standing-table__cell--name-link">Manchester City</a>
    </td>
    <td class="standing-table__cell">4</td>
    <td class="standing-table__cell is-hidden--bp35">4</td>
    <td class="standing-table__cell is-hidden--bp35">0</td>
    <td class="standing-table__cell is-hidden--bp35">0</td>
    <td class="standing-table__cell is-hidden--bp35">11</td>
    <td class="standing-table__cell is-hidden--bp35">2</td>
    <td class="standing-table__cell">9</td>
    <td class="standing-table__cell" data-sort-value="1">12</td>
    <td class="standing-table__cell is-hidden--bp15 is-hidden--bp35 " data-sort-value="123333">
        <div class="standing-table__form">
            <span title="Burnley 0-3 Manchester City" class="standing-table__form-cell standing-table__form-cell--win"> </span>
            <span title="Manchester City 1-0 Newcastle United" class="standing-table__form-cell standing-table__form-cell--win"> </span>
            <span title="Sheffield United 1-2 Manchester City" class="standing-table__form-cell standing-table__form-cell--win"> </span>
            <span title="Manchester City 5-1 Fulham" class="standing-table__form-cell standing-table__form-cell--win"> </span>
            <span class="standing-table__form-cell"> </span>
            <span class="standing-table__form-cell"> </span>
        </div>
    </td>
</tr>
```

This is a snippet of how the HTML code looks like on the [source page](https://www.skysports.com/premier-league-table). The main issue here is that values like Played, Wins, Loses, Goals For, Goals Against, Goal Difference, and Points obtained are under the same class, which can confuse HTML parsers, so I had to use 2 'for' cycles in order to shift rows.

```python
for i in range(1, 21):
    positions = soup.find_all('tr', class_='standing-table__row')[i]
    for position in positions:
        place = positions.find('td', class_='standing-table__cell').text
        name = positions.find('td', class_='standing-table__cell standing-table__cell--name').a.text
```

### Result:

![image](https://github.com/vkogay7/WebScraping_PremierLeagueTable/assets/73743006/416d5d4a-a343-4726-8278-fd218071387a)
```

