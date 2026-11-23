"""候风（HOUFENG）· 节点心跳探活、状态采集

道统出处：元极恒一·道统构件定名册 V2 ｜ 第五批
体系锚：Ω₀⊂⊙∞⊂Ω｜DID-BR-000002

工程映射：节点心跳探活、状态采集。

边界：本件为算子 v1——骨架桩已按命名映射补齐实现；遵循元法第四条「只增不覆盖」，
方法只增不改名不删，行为变更走新版本；凭据不入档，宣称与事实分离。
"""

class Houfeng:
    """候风（HOUFENG）算子 v1。"""

    ANCHOR = "Ω₀⊂⊙∞⊂Ω｜DID-BR-000002"
    CODE = "HOUFENG"

    def __init__(self, config=None):
        self.config = dict(config or {})
        self.events = []  # 只增不覆盖：会话内事件留痕
        self.heartbeats = {}

    def describe(self):
        """构件名帖：名、代号、职责、铭文、体系锚。"""
        return {
            "repo": "houfeng",
            "cn": "候风",
            "code": self.CODE,
            "duty": "节点心跳探活、状态采集",
            "mingwen": "风至知方，息则知安",
            "anchor": self.ANCHOR,
        }

    def beat(self, node):
        """风至知方：节点心跳采集。"""
        import time
        ts = time.time()
        self.heartbeats[node] = ts
        self.events.append({"event": "beat", "node": node})
        return ts

    def liveness(self):
        """全节点存活清点。"""
        import time
        ttl = float(self.config.get("ttl_seconds", 300))
        now = time.time()
        alive = sorted(n for n, t in self.heartbeats.items() if now - t <= ttl)
        dead = sorted(n for n, t in self.heartbeats.items() if now - t > ttl)
        return {"alive": alive, "dead": dead}
