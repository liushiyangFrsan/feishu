# Code generated by Lark OpenAPI.

from .v1.resource import *


class ImService(object):
    def __init__(self, config: Config) -> None:
        self.v1: V1 = V1(config)


class V1(object):
    def __init__(self, config: Config) -> None:
        self.batch_message: Optional[BatchMessage] = BatchMessage(config)
        self.chat: Optional[Chat] = Chat(config)
        self.chat_announcement: Optional[ChatAnnouncement] = ChatAnnouncement(config)
        self.chat_managers: Optional[ChatManagers] = ChatManagers(config)
        self.chat_member_bot: Optional[ChatMemberBot] = ChatMemberBot(config)
        self.chat_member_user: Optional[ChatMemberUser] = ChatMemberUser(config)
        self.chat_members: Optional[ChatMembers] = ChatMembers(config)
        self.chat_menu_item: Optional[ChatMenuItem] = ChatMenuItem(config)
        self.chat_menu_tree: Optional[ChatMenuTree] = ChatMenuTree(config)
        self.chat_moderation: Optional[ChatModeration] = ChatModeration(config)
        self.chat_tab: Optional[ChatTab] = ChatTab(config)
        self.chat_top_notice: Optional[ChatTopNotice] = ChatTopNotice(config)
        self.file: Optional[File] = File(config)
        self.image: Optional[Image] = Image(config)
        self.message: Optional[Message] = Message(config)
        self.message_reaction: Optional[MessageReaction] = MessageReaction(config)
        self.message_resource: Optional[MessageResource] = MessageResource(config)
        self.pin: Optional[Pin] = Pin(config)
        self.special_focus: Optional[SpecialFocus] = SpecialFocus(config)
