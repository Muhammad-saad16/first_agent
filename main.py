from agents import  Agent,Runner
import asyncio
from my_config.conf import MODEL
from my_agents.teachers import chemistry_teacher

async def main():
    result = await Runner.run(chemistry_teacher, "what is the chemical formula of water? ")
    print(result.final_output)

asyncio.run(main())