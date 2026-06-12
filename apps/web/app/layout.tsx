import type { ReactNode } from "react";
import "./globals.css";

export const metadata = {
  title: "Structural AI Inspection System",
  description: "AI-assisted inspection, reporting, and repair prioritization."
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
