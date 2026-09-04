"""Compatibility fixes for dependencies that are no longer maintained."""


def install_pyrogram_peer_id_fix() -> None:
    """Teach Pyrogram 2.0 about channel IDs beyond its old 32-bit limit.

    Telegram Bot API channel/supergroup IDs always start with ``-100``.
    Pyrogram 2.0.106 rejects newer IDs whose internal channel ID is greater
    than 2**31 - 1 before it gets a chance to resolve them from Telegram.
    """
    from pyrogram import utils

    original = utils.get_peer_type
    if getattr(original, "_zelzal_supports_large_channels", False):
        return

    def get_peer_type(peer_id: int):
        try:
            return original(peer_id)
        except ValueError:
            if isinstance(peer_id, int) and str(peer_id).startswith("-100"):
                return "channel"
            raise

    get_peer_type._zelzal_supports_large_channels = True
    utils.get_peer_type = get_peer_type
