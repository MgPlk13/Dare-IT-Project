# Software settings.
### Why I decided to participate in the project?
I decided to try myself in automated testing,
to find my first job in the IT field, as technologies are close and familiar to me
which are used in this work.

## Selectors for exit page:
### Login
* //input[@id='login'] or,
* //*[@id='login'] or
* //*[@id='login']/parent::div
---

### Email
* //div[@class'MuiInputBase-root MuiInput-root MuiInput-underline 
MuiInputBase-formControl MuiInput-formControl']
---
### Go to reminder page password
* //a[contains(text(),'Remind password')]
* //a[starts-with(text(),'Remind')]
---

### Button sing_in
* //button[@type='submit']/span[2] 
* //*[@class='MuiTouchRipple-root']