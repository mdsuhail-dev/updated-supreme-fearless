#pylint:disable=W0702
#pylint:disable=W0612
#pylint:disable=W0104
#pylint:disable=W0613
#pylint:disable=E1101
#pylint:disable=W0611
#pylint:disable=E0213

import time

from telegram.ext.updater import Updater 

from telegram.update import Update 

from telegram.ext.callbackcontext import CallbackContext

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from telegram.ext.commandhandler import CommandHandler 

from telegram.ext.messagehandler import MessageHandler

from telegram.ext import TypeHandler, ContextTypes, CallbackQueryHandler

from telegram.ext import ChatMemberHandler

from telegram import ParseMode

from telegram.ext.filters import Filters

from telegram import Chat, ChatMember, ChatMemberUpdated, ChatPermissions
import logging
from typing import Optional, Tuple

from datetime import date

from googletrans import Translator

import telegram

import emoji

import json 

import requests 

import random

import datetime


  
class MyBot():
	logging.basicConfig(
		format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
		)

	logger = logging.getLogger(__name__)
	owner_id = 1352175396
	
	
	
	mute_list = {}
	ban_list = {}
	
	updater = Updater("5368274717:AAFmwIxfn5OWgQzEicsfrem4v_eCqFDwCX4", use_context=True) 
	api_key = "5368274717:AAFmwIxfn5OWgQzEicsfrem4v_eCqFDwCX4"

	bot = telegram.Bot(token=api_key)
	
	today = date.today()
	
	  
	
 
	 
	
	
		
		

	def main_bot(update: Update, context: CallbackContext):
		api_key = '5368274717:AAFmwIxfn5OWgQzEicsfrem4v_eCqFDwCX4'
		
		now_time = datetime.datetime.now()
		
		try:
			msg = update.message.text
		except:
			pass
		
		msg1 = update.effective_message
		
		msg_id = msg1.message_id
		
		chat = update.effective_chat
		
		chat_id = chat.id
		
		user = update.effective_user
		
		user_id = user.id
		
		bot = telegram.Bot(token=api_key)
		
		admin_status = bot.get_chat_member(chat_id, user_id)
		
		admin_s = admin_status.status
		
		
		
		admin_str = "creator", "administrator"
		
		translator = Translator()
		if "/translate" in msg:
			msg = msg.replace("/translate ", "")
			translated_text = translator. translate(str(msg))
			translated_text = translated_text.text
			
			update.message.reply_text(translated_text)
		if "/p" in msg:
			crypto = ""
			crypto1 = str(msg)
			try:
				key = "https://api.binance.com/api/v3/ticker/price?symbol="
				j = 0
				  
				crypto = str(crypto1.upper())
				crypto = crypto.replace("/P ", "")
				  
				currencies = [crypto]
					
				for i in currencies:
					url = key+currencies[j]
					data = requests.get(url)
			
					data = data.json()
				
					j = j+1
				 	   
				
					update.message.reply_text(f"{data['symbol']} price is {data['price']}{data['symbol']}")
			except:
			   pass
		   
		   
	
		
		if msg == "help":
			update.message.reply_text("""
If You Need Any Help Queries Contact Our Admin. """)
		
		
		if msg == "hi" or msg == "Hi":
			update.message.reply_text(emoji.emojize("""
		Hi, How are You ?"""))
		
		
		if msg == "bot":
			update.message.reply_text(emoji.emojize("""
			Bot is Working :grinning_face_with_smiling_eyes: :smiling_face_with_halo:"""))
			
			
		if "/send" in msg:
			if admin_s in admin_str:
				try:
					message_fromuser = update.effective_message.reply_to_message
				
					last_id = message_fromuser.message_id
					msg_sender = msg
					msg_sender = msg_sender.replace('/send ', '')
					bot.send_message(chat_id, text=msg_sender, reply_to_message_id=last_id)
					bot.delete_message(chat_id, msg_id)
				
				except AttributeError:
					msg_sender = msg
					msg_sender = msg_sender.replace('/send ', '')
					bot.send_message(chat_id, text=msg_sender)
					bot.delete_message(chat_id, msg_id)
					
			
			
			
		if "/game" == msg:
			chat = update.effective_chat
			msg = update.effective_message
			msg_id_m = msg.message_id
			user = update.effective_user
			user_id = user.id
			chat_id = chat.id
			
			api_key = '5368274717:AAFmwIxfn5OWgQzEicsfrem4v_eCqFDwCX4'
		
				
			
			dart = "🎯"
			f_ball = "⚽"
			b_ball = "🏀"
			dice_d = "🎲"
			casino = "🎰"
			ball_b = "🎳"
			num = random.randint(1, 6)
			emj = "🎲"
			if num == 1:
				emj = dart
			elif num == 2:
				emj = f_ball
			elif num == 3:
				emj = b_ball
			elif num == 4:
				emj = dice_d
			elif num == 5:
				emj = casino
			elif num == 6:
				emj = ball_b
		
			bot = telegram.Bot(token=api_key)
			bot_id_msg = bot.send_dice(chat_id, emoji=emj)
			
			
			time.sleep(5)
			bot.delete_message(chat_id, msg_id_m)
			bot_id_msg.delete()
			
			
			
		
		if "/show_chats" == msg:
			user_ids = ", ".join(str(uid) for uid in context.bot_data.setdefault("user_ids", set()))
			group_ids = ", ".join(str(gid) for gid in context.bot_data.setdefault("group_ids", set()))
			channel_ids = ", ".join(str(cid) for cid in context.bot_data.setdefault("channel_ids", set()))
			text = (
		        f"@{context.bot.username} is currently in a conversation with the user IDs {user_ids}."
		        f" Moreover it is a member of the groups with IDs {group_ids} "
		        f"and administrator in the channels with IDs {channel_ids}."
		    )
			update.effective_message.reply_text(text)	
				
					
			
		if "/ban" == msg:
			if admin_s in admin_str:
				try:
					bnd = update.effective_message.reply_to_message.from_user
					a_men = """<a href="tg://user?id="""
					a_men += str(bnd.id) + """">"""
					mention_text = a_men + bnd.first_name + "</a>"
					bnd_id = bnd.id
					print("work")
					if bnd_id != 5376177894:
						try:
							print("yaha ")
							if chat_id not in MyBot.ban_list:
								MyBot.ban_list[chat_id] = {}
									
							a_byban = """<a href="tg://user?id="""
							a_byban += str(user_id) + """">"""
							mention_new = a_byban + user.first_name + "</a>"
							new_time = str(now_time.date) + " " + str(now_time.hour) + ":" + str(now_time.minute) + ":" + str(now_time.second)
							print("tak")
							if bnd_id not in MyBot.ban_list[chat_id]:
								print("done")
								bot.ban_chat_member(chat_id, bnd_id)
								print("haii")
								MyBot.ban_list[chat_id][bnd_id] = f"""Banned Time and Date: {new_time}
		 Banned By: {mention_new}"""
								print("fit")
								print(mention_text, "\n\n", mention_new)
								update.message.reply_text(f"""Read The Rules,
								
	Succesfully Banned {mention_text}""",parse_mode=ParseMode.HTML,)
								print("done hai")
	
									
									
							
							elif bnd_id in MyBot.ban_list[chat_id]:
								update.message.reply_text(f"""{mention_text} is Already Banned, Try /unban to Unban Him.""", parse_mode=ParseMode.HTML,)
						
						except telegram.error.BadRequest:
							update.message.reply_text("I don't have rights to ban admin.' 💀")
						
						except AttributeError:
							update.message.reply_text("What ? I Dont Know Which User Do You Want To Ban, Reply Him And Type Command Again ")
					
				except AttributeError:
					update.message.reply_text("I Dont Know Which User You Say ?, Reply Him and Try Again.")
		
		if "/mute" == msg:
			if admin_s in admin_str:
				try:
					bnd = update.effective_message.reply_to_message.from_user
					#bndt = update.effective_message.reply_to_message
					a_men = """<a href="tg://user?id="""
					a_men += str(bnd.id) + """">"""
					mention_text = a_men + bnd.first_name + "</a>"
					bnd_id = bnd.id
					if bnd_id != 5376177894:
						if chat_id not in MyBot.mute_list:
							MyBot.mute_list[chat_id] = {}
								
						permissions = ChatPermissions(can_send_messages=False)
						
						if bnd_id not in MyBot.mute_list[chat_id]:
							bot.restrict_chat_member(chat_id, bnd_id, permissions)
							a_byban = """<a href="tg://user?id="""
							a_byban += str(user_id) + """">"""
							mention_new = a_byban + user.first_name + "</a>"
							new_time = str(now_time.date) + " " + str(now_time.hour) + ":" + str(now_time.minute) + ":" + str(now_time.second)
							MyBot.mute_list[chat_id][bnd_id] = f"""Muted Date: {new_time}
	Muted By: {mention_new}"""
							update.message.reply_text(f"""Succesfully Muted {mention_text}""",parse_mode=ParseMode.HTML,)
								
						elif bnd_id in MyBot.mute_list[chat_id]:
								update.message.reply_text(f"""{mention_text} Already Mute
								
	{MyBot.mute_list[chat_id][bnd_id]}""",parse_mode=ParseMode.HTML,)
	
				except telegram.error.BadRequest:
					update.message.reply_text("I Don't Have Rights to Mute A Admin.")
				except AttributeError:
					update.message.reply_text("I Dont Know Which User You Say ?, Reply Him and Try Again.")
						
						
			
		
		
		
		
		
		if "/unban" == msg:
			if admin_s in admin_str:
				try:
					bnd = update.effective_message.reply_to_message.from_user
					bnd_id = bnd.id
					a_men = """<a href="tg://user?id="""
					a_men += str(bnd.id) + """">"""
					mention_text = a_men + bnd.first_name + "</a"
					mention_text += ">"
					nm_id = bnd.username
					nm_name = bnd.first_name
					if bnd_id != 5376177894:
						print("1")
						print(chat_id)
						print(bnd_id)
						try:
							if bnd_id in MyBot.ban_list[chat_id]:
								if "Banned" in MyBot.ban_list[chat_id][bnd_id]:
									bot.unban_chat_member(chat_id, bnd_id)
									MyBot.ban_list[chat_id][bnd_id] = "User Unban."
									update.message.reply_text(f"""{mention_text} is Successfully Unban,
				Now {mention_text} is Join Group Again,
				and Read The Rules """,parse_mode=ParseMode.HTML,)
				
							else:
								update.message.reply_text(f"""{mention_text} is Not Banned. """,parse_mode=ParseMode.HTML,)
						except Exception:
							update.message.reply_text(f"""{mention_text} is Not Banned. """,parse_mode=ParseMode.HTML,)
							
							
				except AttributeError:
					update.message.reply_text("I Dont Know Which User You Say ?, Reply Him and Try Again.")
					
				except telegram.error.BadRequest:
					update.message.reply_text("How Can I Unban Admin, You Don't KnowAdmin is Not Banned.")
				
				
				
				
		if "/unmute" == msg:
			if admin_s in admin_str:
				print("r")
				try:
					bnd = update.effective_message.reply_to_message.from_user
					bnd_id = bnd.id
					a_men = """<a href="tg://user?id="""
					a_men += str(bnd.id) + """">"""
					mention_text = a_men + bnd.first_name + "</a"
					mention_text += ">"
					if bnd_id != 5376177894:
						if bnd_id in MyBot.mute_list[chat_id]:
							if "Muted" in MyBot.mute_list[chat_id][bnd_id]:
								permissions = ChatPermissions(can_send_messages=True)
								bot.restrict_chat_member(chat_id, bnd_id, permissions)
								MyBot.mute_list[chat_id][bnd_id] = "User Unmute."
								update.message.reply_text(f"""{mention_text} is Successfully Unmute.""",parse_mode=ParseMode.HTML,)
							
				except AttributeError:
					update.message.reply_text("I Dont Know Which User You Say ?, Reply Him and Try Again.")
					
				except telegram.error.BadRequest:
					update.message.reply_text("How Can I Unmute Admin, You Don't Know Admin is Not Mute.")
				
				except Exception:
					print("done")
					update.message.reply_text("This Person is already free..")
			
			
	def extract_status_change(chat_member_update: ChatMemberUpdated) -> Optional[Tuple[bool, bool]]:
		status_change = chat_member_update.difference().get("status")
		
		old_is_member, new_is_member = chat_member_update.difference().get("is_member", (None, None))
		
		if status_change is None:
			return None
		
		old_status, new_status = status_change
		was_member = old_status in [
			ChatMember.MEMBER,
			ChatMember.CREATOR,
			ChatMember.ADMINISTRATOR,
		] or (old_status == ChatMember.RESTRICTED and old_is_member is True)
		
		is_member = new_status in [
			ChatMember.MEMBER,
			ChatMember.CREATOR,
			ChatMember.ADMINISTRATOR,
		] or (new_status == ChatMember.RESTRICTED and new_is_member is True)
		
		return was_member, is_member


	def track_chats(update: Update, context: ContextTypes):
	    """Tracks the chats the bot is in."""
	    result = MyBot.extract_status_change(update.my_chat_member)
	    
	    if result is None:
	        return
	    was_member, is_member = result
	
	    # Let's check who is responsible for the change
	    cause_name = update.effective_user.full_name
	
	    # Handle chat types differently:
	    chat = update.effective_chat
	    if chat.type == Chat.PRIVATE:
	        if not was_member and is_member:
	            MyBot.logger.info("%s started the bot", cause_name)
	            a = context.bot_data.setdefault("user_ids", set()).add(chat.id)
	            
	        elif was_member and not is_member:
	           MyBot. logger.info("%s blocked the bot", cause_name)
	           context.bot_data.setdefault("user_ids", set()).discard(chat.id)
	    elif chat.type in [Chat.GROUP, Chat.SUPERGROUP]:
	        if not was_member and is_member:
	            MyBot.logger.info("%s added the bot to the group %s", cause_name, chat.title)
	            context.bot_data.setdefault("group_ids", set()).add(chat.id)
	            v = "Added The Bot To The Group \n\n"
	            names_g =  cause_name
	            name_c = chat.title
	            name_d = chat.id
	            user_name = chat.username
	            spce = "\n"
	            names_g = str(names_g)
	            name_c = str(name_c)
	            name_d = str(name_d)
	            user_user = update.effective_user.username
	            user_id = update.effective_user.id
	            if user_name != None or user_user != None:
	            	v += names_g + spce + name_c + spce + name_d + spce + "@" + user_user + spce + "@" + user_name
	            elif user_name == None:
	            	v += names_g + spce + "User Id: " + user_id + spce + name_c + spce + "Chat Id: " + name_d
	            v = str(v)
	            MyBot.bot.send_message(1352175396, v)
	        elif was_member and not is_member:
	            context.bot_data.setdefault("group_ids", set()).discard(chat.id)
	            context.bot_data.setdefault("group_ids", set()).discard(chat.id)
	    else:
	        if not was_member and is_member:
	            MyBot.logger.info("%s added the bot to the channel %s", cause_name, chat.title)
	            context.bot_data.setdefault("channel_ids", set()).add(chat.id)
	        elif was_member and not is_member:
	            MyBot.logger.info("%s removed the bot from the channel %s", cause_name, chat.title)
	            context.bot_data.setdefault("channel_ids", set()).discard(chat.id)
	            
	            
	            
	def greet_chat_members(update: Update, context: ContextTypes):
	    """Greets new users in chats and announces when someone leaves"""
	    result = MyBot.extract_status_change(update.chat_member)
	    if result is None:
	        return
	
	    was_member, is_member = result
	    cause_name = update.chat_member.from_user.mention_html()
	    member_name = update.chat_member.new_chat_member.user.mention_html()
	    
	    
	    chat_m = update.effective_chat
	    chat_name = chat_m.title
	    if not was_member and is_member:
	        if cause_name == member_name:
	        	update.effective_chat.send_message(
	            f"{member_name} Welcome! to {chat_name}",parse_mode=ParseMode.HTML,)
	        if cause_name != member_name:	
	        	update.effective_chat.send_message(
	            f"{member_name} was added by {cause_name}. Welcome!",parse_mode=ParseMode.HTML,)
	    elif was_member and not is_member:
	        if cause_name == member_name:
	        	update.effective_chat.send_message(
	            f"{member_name} is no longer with us. Thanks a lot",parse_mode=ParseMode.HTML,)
	        	
	        if cause_name != member_name:
	        	update.effective_chat.send_message(
	            f"{member_name} is no longer with us. Thanks a lot, Removed By {cause_name}",parse_mode=ParseMode.HTML,)
	
	
			
		
		 	
		
		
				
			
			
			
	updater.dispatcher.add_handler(ChatMemberHandler(track_chats, ChatMemberHandler.MY_CHAT_MEMBER))
	
	updater.dispatcher.add_handler(ChatMemberHandler(greet_chat_members, ChatMemberHandler.CHAT_MEMBER))
	
	updater.dispatcher.add_handler(MessageHandler(Filters.text, main_bot))
	updater.start_polling()
	
MyBot()