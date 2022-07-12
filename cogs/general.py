from disnake.ext import commands
import asyncio
import disnake
import sqlite3

database = sqlite3.connect('server.db')
cursor = database.cursor()


def delete_database(objects):
    cursor.execute("DELETE FROM profile WHERE id = {}".format(objects))
    database.commit()


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="создать", description="Создать профиль на сервере")
    async def create_profile(self, inter):

        if cursor.execute(f"SELECT id FROM profile WHERE id = {inter.author.id}").fetchone() is not None:
            embed = disnake.Embed(description="**ты не можешь иметь более одного профиля на сервере**", colour=0x36393f)
            return await inter.send(embed=embed)

        if cursor.execute(f"SELECT id FROM blacklist WHERE id = {inter.author.id}").fetchone() is not None:
            embed = disnake.Embed(description="**Ты не можешь создать профиль так как ты в ЧС**", colour=0x36393f)
            return await inter.send(embed=embed, ephemeral=True)

        await inter.send("Добро пожаловать, сэр! Представьтесь, пожалуйста.")

        try:
            message = await self.bot.wait_for("message", check=lambda m:
            m.author == inter.author and m.channel == inter.channel, timeout=30.0)

        except asyncio.TimeoutError:
            await inter.channel.send("Время вышло, попробуй заново использовать команду.")
            delete_database(inter.author.id)

        else:
            name = message.content
            await inter.channel.send(f"Добро пожаловать, в команду новобранец! Какой твой игровой никнейм?")
            cursor.execute(f"INSERT INTO profile (id, member) VALUES ({inter.author.id}, '{name}')")
            database.commit()
            try:
                message = await self.bot.wait_for("message", check=lambda m:
                m.author == inter.author and m.channel == inter.channel, timeout=30.0)

            except asyncio.TimeoutError:
                await inter.channel.send("Время вышло, попробуй заново использовать команду.")
                delete_database(inter.author.id)

            else:

                nickname = message.content
                senc = f"**{nickname}**, Желаешь ли ты участвовать в полковых реалистичных событиях? (Да/Нет)"
                await inter.channel.send(senc)
                sql = f"UPDATE profile SET nickname = ? WHERE id = ?"
                val = (nickname, inter.author.id)
                cursor.execute(sql, val)
                database.commit()

                try:
                    message = await self.bot.wait_for("message", check=lambda m:
                    m.author == inter.author and m.channel == inter.channel, timeout=30.0)

                except asyncio.TimeoutError:
                    await inter.channel.send("Время вышло, попробуй заново использовать команду.")
                    delete_database(inter.author.id)

                else:

                    if message.content.lower() == "да":
                        polk_yes = "Супер! В какой полк ты бы хотел вступить? подробнее тут <#982047222931783701>"
                        cursor.execute(f"UPDATE profile SET realistic_events = 'да' WHERE id = {inter.author.id}")
                        database.commit()
                        await inter.channel.send(polk_yes)

                    elif message.content.lower() == "нет":
                        cursor.execute(f"UPDATE profile SET realistic_events = 'нет' WHERE id = {inter.author.id}")
                        database.commit()
                        polk = "Жаль конечно. Тогда выбери себе полк тут <#982047222931783701>, после напиши его"
                        await inter.channel.send(polk)

                    else:

                        error = "Я тебя не понимаю, возможно ты где то что то не так сказал."
                        await inter.channel.send(error)
                        delete_database(inter.author.id)

                    try:
                        message = await self.bot.wait_for("message", check=lambda m:
                        m.author == inter.author and m.channel == inter.channel, timeout=60.0)

                    except asyncio.TimeoutError:
                        await inter.channel.send("Время вышло, попробуй заново использовать команду.")
                        delete_database(inter.author.id)

                    else:
                        if message.content == "WarCA":
                            role = inter.guild.get_role(982008126372990986)
                            await inter.author.add_roles(role)
                            await inter.send("**Принято. Ожидай, составляем анкету!**")
                            sql = f"UPDATE profile SET regiment = ? WHERE id = ?"
                            val = ("WarCA", inter.author.id)
                            cursor.execute(sql, val)
                            database.commit()

                        elif message.content == "KOKA":
                            role = inter.guild.get_role(908770702654603275)
                            await inter.author.add_roles(role)
                            await inter.send("**Принято. Ожидай, составляем анкету!**")
                            sql = f"UPDATE profile SET regiment = ? WHERE id = ?"
                            val = ("KOKA", inter.author.id)
                            cursor.execute(sql, val)
                            database.commit()

                        elif message.content == "030H":
                            role = inter.guild.get_role(835295093413117963)
                            await inter.author.add_roles(role)
                            await inter.send("**Принято. Ожидай, составляем анкету!**")
                            sql = f"UPDATE profile SET regiment = ? WHERE id = ?"
                            val = ("030H", inter.author.id)
                            cursor.execute(sql, val)
                            database.commit()

                        elif message.content == "03OH":
                            role = inter.guild.get_role(842397142105456650)
                            await inter.author.add_roles(role)
                            await inter.send("**Принято. Ожидай, составляем анкету!**")
                            sql = f"UPDATE profile SET regiment = ? WHERE id = ?"
                            val = ("03OH", inter.author.id)
                            cursor.execute(sql, val)
                            database.commit()

                        elif message.content == "DSRTR":
                            role = inter.guild.get_role(908770817649819678)
                            await inter.author.add_roles(role)
                            await inter.send("**Принято. Ожидай, составляем анкету!**")
                            sql = f"UPDATE profile SET regiment = ? WHERE id = ?"
                            val = ("DSRTR", inter.author.id)
                            cursor.execute(sql, val)
                            database.commit()

                        elif message.content == "IIUBO":
                            role = inter.guild.get_role(917299607187386379)
                            await inter.author.add_roles(role)
                            await inter.send("**Принято. Ожидай, составляем анкету!**")
                            sql = f"UPDATE profile SET regiment = ? WHERE id = ?"
                            val = ("IIUBO", inter.author.id)
                            cursor.execute(sql, val)
                            database.commit()

                        elif message.content == "R384":
                            role = inter.guild.get_role(938458899458191440)
                            await inter.author.add_roles(role)
                            await inter.send("**Принято. Ожидай, составляем анкету!**")
                            sql = f"UPDATE profile SET regiment = ? WHERE id = ?"
                            val = ("R384", inter.author.id)
                            cursor.execute(sql, val)
                            database.commit()

                        elif message.content == "METAH":
                            role = inter.guild.get_role(959725281055232041)
                            await inter.author.add_roles(role)
                            await inter.send("**Принято. Ожидай, составляем анкету!**")
                            sql = f"UPDATE profile SET regiment = ? WHERE id = ?"
                            val = ("METAH", inter.author.id)
                            cursor.execute(sql, val)
                            database.commit()

                        elif message.content == "A3OT":
                            role = inter.guild.get_role(959812860563820564)
                            await inter.author.add_roles(role)
                            await inter.send("**Принято. Ожидай, составляем анкету!**")
                            sql = f"UPDATE profile SET regiment = ? WHERE id = ?"
                            val = ("A3OT", inter.author.id)
                            cursor.execute(sql, val)
                            database.commit()

                        elif message.content == "PolBu":
                            role = inter.guild.get_role(959714360853409802)
                            await inter.author.add_roles(role)
                            await inter.send("**Принято. Ожидай, составляем анкету!**")
                            sql = f"UPDATE profile SET regiment = ? WHERE id = ?"
                            val = ("PolBu", inter.author.id)
                            cursor.execute(sql, val)
                            database.commit()

                        elif message.content == "PTyTb":
                            role = inter.guild.get_role(959813799861420093)
                            await inter.author.add_roles(role)
                            await inter.send("**Принято. Ожидай, составляем анкету!**")
                            sql = f"UPDATE profile SET regiment = ? WHERE id = ?"
                            val = ("PTyTb", inter.author.id)
                            cursor.execute(sql, val)
                            database.commit()

                        elif message.content == "OKTAH":
                            role = inter.guild.get_role(982008126372990986)
                            await inter.author.add_roles(role)
                            await inter.send("**Принято. Ожидай, составляем анкету!**")
                            sql = f"UPDATE profile SET regiment = ? WHERE id = ?"
                            val = ("OKTAH", inter.author.id)
                            cursor.execute(sql, val)
                            database.commit()

                        elif message.content == "HEOH":
                            role = inter.guild.get_role(959813901824954379)
                            await inter.author.add_roles(role)
                            await inter.send("**Принято. Ожидай, составляем анкету!**")
                            sql = f"UPDATE profile SET regiment = ? WHERE id = ?"
                            val = ("HEOH", inter.author.id)
                            cursor.execute(sql, val)
                            database.commit()

                        elif message.content == "Hired":
                            role = inter.guild.get_role(959813544206020618)
                            await inter.author.add_roles(role)
                            await inter.send("**Принято. Ожидай, составляем анкету!**")
                            sql = f"UPDATE profile SET regiment = ? WHERE id = ?"
                            val = ("Hired", inter.author.id)
                            cursor.execute(sql, val)
                            database.commit()

                        elif message.content == "XPOM":
                            role = inter.guild.get_role(959814000902811678)
                            await inter.author.add_roles(role)
                            await inter.send("**Принято. Ожидай, составляем анкету!**")
                            sql = f"UPDATE profile SET regiment = ? WHERE id = ?"
                            val = ("XPOM", inter.author.id)
                            cursor.execute(sql, val)
                            database.commit()

                        elif message.content == "XJIOP":
                            role = inter.guild.get_role(959814088584757338)
                            await inter.author.add_roles(role)
                            await inter.send("**Принято. Ожидай, составляем анкету!**")
                            sql = f"UPDATE profile SET regiment = ? WHERE id = ?"
                            val = ("XJIOP", inter.author.id)
                            cursor.execute(sql, val)
                            database.commit()

                        elif message.content == "ZomCa":
                            role = inter.guild.get_role(959813657141850124)
                            await inter.author.add_roles(role)
                            await inter.send("**Принято. Ожидай, составляем анкету!**")
                            sql = f"UPDATE profile SET regiment = ? WHERE id = ?"
                            val = ("ZomCa", inter.author.id)
                            cursor.execute(sql, val)
                            database.commit()

                        elif message.content == "KAPAT":
                            role = inter.guild.get_role(959813461964103680)
                            await inter.author.add_roles(role)
                            await inter.send("**Принято. Ожидай, составляем анкету!**")
                            sql = f"UPDATE profile SET regiment = ? WHERE id = ?"
                            val = ("KAPAT", inter.author.id)
                            cursor.execute(sql, val)
                            database.commit()

                        elif message.content == "Manic":
                            role = inter.guild.get_role(959813384386248704)
                            await inter.author.add_roles(role)
                            await inter.send("**Принято. Ожидай, составляем анкету!**")
                            sql = f"UPDATE profile SET regiment = ? WHERE id = ?"
                            val = ("Manic", inter.author.id)
                            cursor.execute(sql, val)
                            database.commit()

                        elif message.content == "OTPOK":
                            role = inter.guild.get_role(959813718210904114)
                            await inter.author.add_roles(role)
                            await inter.send("**Принято. Ожидай, составляем анкету!**")
                            sql = f"UPDATE profile SET regiment = ? WHERE id = ?"
                            val = ("OTPOK", inter.author.id)
                            cursor.execute(sql, val)
                            database.commit()

                        elif message.content == "NAMI":
                            role = inter.guild.get_role(959813299065716756)
                            await inter.author.add_roles(role)
                            await inter.send("**Принято. Ожидай, составляем анкету!**")
                            sql = f"UPDATE profile SET regiment = ? WHERE id = ?"
                            val = ("NAMI", inter.author.id)
                            cursor.execute(sql, val)
                            database.commit()

                        elif message.content == "RUBY":
                            role = inter.guild.get_role(954079334660988931)
                            await inter.author.add_roles(role)
                            await inter.send("**Принято. Ожидай, составляем анкету!**")
                            sql = f"UPDATE profile SET regiment = ? WHERE id = ?"
                            val = ("RUBY", inter.author.id)
                            cursor.execute(sql, val)
                            database.commit()

                        elif message.content == "Valve":
                            role = inter.guild.get_role(963431563784224808)
                            await inter.author.add_roles(role)
                            await inter.send("**Принято. Ожидай, составляем анкету!**")
                            sql = f"UPDATE profile SET regiment = ? WHERE id = ?"
                            val = ("Valve", inter.author.id)
                            cursor.execute(sql, val)
                            database.commit()

                        elif message.content == "AGFT":
                            role = inter.guild.get_role(980877683250569297)
                            await inter.author.add_roles(role)
                            await inter.send("**Принято. Ожидай, составляем анкету!**")
                            sql = f"UPDATE profile SET regiment = ? WHERE id = ?"
                            val = ("AGFT", inter.author.id)
                            cursor.execute(sql, val)
                            database.commit()

                        elif message.content == "друг альянса":
                            role = inter.guild.get_role(982008126372990986)
                            await inter.author.add_roles(role)
                            await inter.send("**Принято. Ожидай, составляем анкету!**")
                            sql = f"UPDATE profile SET regiment = ? WHERE id = ?"
                            val = ("друг альянса", inter.author.id)
                            cursor.execute(sql, val)
                            database.commit()

                        elif message.content == "дипломат":
                            role = inter.guild.get_role(982008126372990986)
                            await inter.author.add_roles(role)
                            await inter.send("**Принято. Ожидай, составляем анкету!**")
                            await asyncio.sleep(2)
                            sql = f"UPDATE profile SET regiment = ? WHERE id = ?"
                            val = ("дипломат", inter.author.id)
                            cursor.execute(sql, val)
                            database.commit()

        NAME = cursor.execute(f"SELECT member FROM profile WHERE id = {inter.author.id}").fetchone()[0]
        PLAYER_NICKNAME = cursor.execute(f"SELECT nickname FROM profile WHERE id = {inter.author.id}").fetchone()[0]
        nick = f"<{PLAYER_NICKNAME}>({NAME})"
        await inter.author.edit(nick=nick)

    @commands.slash_command(name="профиль", description="Просмотреть свой профиль на сервере")
    async def profile(self, inter):
        name = cursor.execute(f"SELECT member FROM profile WHERE id = {inter.author.id}").fetchone()[0]
        nickname = cursor.execute(f"SELECT nickname FROM profile WHERE id = {inter.author.id}").fetchone()[0]
        event = cursor.execute(f"SELECT realistic_events FROM profile WHERE id = {inter.author.id}").fetchone()[0]
        polk = cursor.execute(f"SELECT regiment FROM profile WHERE id = {inter.author.id}").fetchone()[0]

        embed = disnake.Embed(colour=0x36393f)
        embed.set_author(name=f"Профиль - {inter.author}", icon_url=inter.author.display_avatar.url)
        embed.add_field(name="`ID`", value=inter.author.id, inline=False)
        embed.add_field(name="`Имя`", value=name, inline=False)
        embed.add_field(name="`Никнейм`", value=nickname, inline=False)
        embed.add_field(name="`События`", value=event, inline=False)
        embed.add_field(name="`Полк`", value=polk, inline=False)
        embed.set_thumbnail(url=inter.author.display_avatar.url)
        await inter.send(embed=embed)

    @commands.slash_command(name="добавить-в-чс", description="Добавить участника в черный список")
    async def add_blacklist(self, inter, user: disnake.Member = commands.param(name="пользователь",
                                                                               description="пользователь для ЧС"),
                            reason=commands.param(name="причина", description="причина для ЧС")):

        cursor.execute(f"INSERT INTO blacklist (id, reason) VALUES ({user.id}, '{reason}')")
        database.commit()
        embed = disnake.Embed(description="**Пользователь добавлен в черный список**", colour=0x36393f)
        await inter.send(embed=embed)

    @commands.slash_command(name="черный-список", description="Просмотр черного списка")
    async def blacklist(self, inter):
        embed = disnake.Embed(description="**Черный список сервера**", colour=0x36393f)
        for row in cursor.execute("SELECT id, reason FROM blacklist"):
            embed.add_field(name=f'ID: {row[0]}', value=f'Причина: **{row[1]}**', inline=False)
        await inter.send(embed=embed)

    @commands.slash_command(name="удалить-из-чс", description="Удаление из черного списка")
    async def remove_blacklist(self, inter, member: disnake.Member = commands.param(name="пользователь",
                                                                                    description="юзер для выноса из ЧС")):
        cursor.execute("DELETE FROM blacklist WHERE id = {}".format(member.id))
        database.commit()
        embed = disnake.Embed(description="**Пользователь удален из черного списка**", colour=0x36393f)
        await inter.send(embed=embed)


def setup(bot):
    bot.add_cog(General(bot))
