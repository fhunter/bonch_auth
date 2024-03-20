%include header
%import settings
<h1>Вход в систему кафедры ПИВТ</h1>
<form method="post" action="{{settings.PREFIX}}/">
<label for="username">Имя пользователя:</label><br>
<input type="text" id="username" name="username"><br>
<label for="password">Пароль:</label><br>
<input type="password" id="password" name="password"><br>
<input type="submit" value="Submit">
</form>
<br>
%include menu
%include footer
