'use client'

import { Card, CardContent, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { useChat } from 'ai/react'
import { Input } from "@/components/ui/input";
import { ScrollArea } from "./ui/scroll-area";

export default function Chat() {
  const { messages, input, handleInputChange, handleSubmit } = useChat({
    api: '/api/chat',
  });

  return (
    <Card className="w-[540px]">
        <CardHeader>
          <CardTitle>Poetry AI</CardTitle>
        </CardHeader>
        <CardContent>
          <ScrollArea className="h-[640px] pr-4">
            {messages.map((message) => (
              <div className="flex gap-3 text-slate-600 mb-4 text-sm" key={message.id}>
                {message.role === 'user' 
                  ? (
                    <Avatar>
                      <AvatarFallback>RF</AvatarFallback>
                      <AvatarImage src="https://github.com/rofram.png" />
                    </Avatar>
                  )
                  : (
                    <Avatar>
                      <AvatarFallback>AI</AvatarFallback>
                      <AvatarImage src="https://github.com/openai.png" />
                    </Avatar>
                  )}
                <p className="leading-relaxed">
                  <b className="block font-bold text-slate-700">{message. role === 'user' ? 'User' : 'Poetry'}:</b>
                  {message.content}
                </p>
              </div>
            ))}
          </ScrollArea>
        </CardContent>
        <CardFooter>
            <form className="flex w-full gap-2" onSubmit={handleSubmit}>
              <Input placeholder="how do you want me to create your poem?" value={input} onChange={handleInputChange} />
              <Button type="submit">Send</Button>
            </form>
        </CardFooter>
      </Card>
  )
}