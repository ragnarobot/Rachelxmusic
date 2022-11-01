from pyrogram.errors import PeerIdInvalid, UserNotParticipant
from Music.MusicUtilities.tgcallsrun.music import pytgcalls, smexy as user
from Music import LOG_GROUP_ID

Bl_Chat = [
    LOG_GROUP_ID,
    -1001638078842,  # support
]

async def leave_from_inactive_call():
    all_chat_id = []
    async for chat in user.iter_dialogs():
        chat_id = chat.chat.id
        if chat.chat.type in ["group", "supergroup"]:
            for call in pytgcalls.calls:
                call_chat_id = int(getattr(call, "chat_id"))
                if call_chat_id in all_chat_id:
                    pass
                else:
                    all_chat_id.append(call_chat_id)
                call_status = getattr(call, "status")
                try:
                    if call_chat_id == chat_id and call_status == "not_playing":
                        await user.leave_chat(chat_id)
                    elif chat_id not in Bl_Chat:
                        await user.leave_chat(chat_id)
                except UserNotParticipant:
                    pass
            if chat_id not in Bl_Chat:
                try:
                    await user.leave_chat(chat_id)
                except (PeerIdInvalid, UserNotParticipant):
                    pass
                  
