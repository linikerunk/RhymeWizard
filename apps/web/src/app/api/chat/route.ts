import { StreamingTextResponse } from "ai";

// IMPORTANT! Set the runtime to edge
// export const runtime = 'edge'

export async function POST(req: Request) {
  const { messages } = await req.json();
  const response = await fetch(process.env.BACK_URL + "/poetry", {
    method: "POST",
    body: JSON.stringify({ messages }),
    headers: { "Content-Type": "application/json" },
  });

  // Respond with the stream
  return new StreamingTextResponse(response.body);
}
