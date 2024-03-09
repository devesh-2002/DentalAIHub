"use client"
import React, { useState } from 'react';
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '@/components/ui/card';
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar';
import { Input } from '@/components/ui/input';
import { Button } from '@/components/ui/button';
import { ScrollArea } from '@/components/ui/scroll-area';

export default function Chat() {
  const [messages, setMessages] = useState<{ id: number, role: string, content: string }[]>([]);
  const [input, setInput] = useState('');

  const simulateAIResponse = (input: string) => {
    return 'This is a simulated response from the AI.';
  };

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setInput(e.target.value);
  };

  const handleSimulatedSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const response = simulateAIResponse(input);
    
    setMessages(prevMessages => [
      ...prevMessages,
      { id: prevMessages.length, role: 'user', content: input }
    ]);

    setMessages(prevMessages => [
      ...prevMessages,
      { id: prevMessages.length, role: 'assistant', content: response }
    ]);

    setInput('');
  };

  return (
    <div className="flex justify-center items-center h-screen">
      <Card className="w-[440px]">
        <CardHeader>
          <CardTitle>Dental Chat AI</CardTitle>
          <CardDescription>Chat me anything about Dental Health</CardDescription>
        </CardHeader>
        <CardContent>
          <ScrollArea className="h-[300px] w-full pr-4">
            {messages.map(message => (
              <div key={message.id} className="flex gap-3 text-slate-600 text-sm mb-4">
                {message.role === 'user' && (
                  <Avatar>
                    <AvatarFallback>TP</AvatarFallback>
                    <AvatarImage src="https://github.com/tamirespatrocinio.png" />
                  </Avatar>
                )}
                {message.role === 'assistant' && (
                  <Avatar>
                    <AvatarImage src="https://github.com/shadcn.png" />
                  </Avatar>
                )}

                <p className="leading-relaxed">
                  <span className="block font-bold text-slate-700">
                    {message.role === 'user' ? 'Usuário' : 'AI'}
                  </span>
                  {message.content}
                </p>
              </div>
            ))}
          </ScrollArea>
        </CardContent>
        <CardFooter>
          <form className="w-full flex gap-2" onSubmit={handleSimulatedSubmit}>
            <Input placeholder="How Can I help you?" value={input} onChange={handleInputChange} />
            <Button type="submit">Send</Button>
          </form>
        </CardFooter>
      </Card>
    </div>
  );
}
