from pydantic import BaseModel,Field
from typing import Optional,Literal
class Student(BaseModel):
    name:str ='KK Bhai'
    age:Optional[int]= None
    agpa:float = Field(gt=0,le=10, default=7.5)


new_student = {'age':'20'}

student = Student(**new_student)
# print(student.name) 
# print(student.age)


from pydantic import BaseModel
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

#SCHEMA
class Review(BaseModel):
    key_themes: list[str] = Field(description="Write down all the key themes in a list")
    summary: str = Field(description="A brief summary of the review")
    sentiment:Literal["pos","neg"] = Field(description="Return sentiment of the review either negative, positive or neutral")
    pros: Optional[list[str]] = Field(default=None,description="Write down all the pros." )
    cons: Optional[list[str]] = Field(default=None,description="Write down all the cons." )
    

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")

)

structured_llm = llm.with_structured_output(Review)

result = structured_llm.invoke(
    """
    The ASUS TUF Gaming A15 is a popular gaming laptop designed for gamers, students, and professionals who need strong performance at a reasonable price. 
    Powered by AMD Ryzen processors and NVIDIA GeForce RTX graphics, the laptop delivers excellent gaming and multitasking capabilities while maintaining 
    ASUS's TUF-series durability standards. Recent models offer high-refresh-rate displays, DDR5 memory support, and upgradeable storage, making them suitable 
    for modern gaming and productivity workloads.

    One of the biggest strengths of the TUF Gaming A15 is its performance-to-price ratio. The laptop can handle demanding games, programming tasks, video editing,
    and content creation efficiently. Many reviewers also praise its durable build quality, good thermal design, upgradeability, and strong battery life compared to 
    other gaming laptops in the same segment.

    However, the laptop is not without compromises. Depending on the configuration, some models may have average display quality, noticeable fan noise during heavy gaming, 
    and a relatively bulky design compared to premium gaming laptops. The speakers and trackpad are also considered average by some reviewers.

    Pros
    Excellent gaming performance for the price.
    Powerful AMD Ryzen processors and NVIDIA RTX graphics.
    Durable military-grade build quality.
    Upgradeable RAM and SSD storage.
    High-refresh-rate display options (144Hz/165Hz).
    Good battery life for a gaming laptop.
    Wide range of connectivity ports.
    Cons
    Fans can become noisy during intensive gaming.
    Heavier than many ultrabooks and premium laptops.
    Display quality varies by configuration.
    Speakers and touchpad are average.
    Design may feel bulky for users seeking portability.
    Conclusion

    The ASUS TUF Gaming A15 is an excellent choice for users seeking a reliable and affordable gaming laptop. It offers strong performance, durability, 
    and upgradeability while keeping costs lower than many premium gaming competitors. Although it has some compromises in portability and display quality, 
    it remains one of the best value-for-money gaming laptops in its category.
    """
)

print(result)