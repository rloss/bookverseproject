'use client'
export default function Home() {
  return (
    <section className="space-y-6">
      <h1 className="text-2xl font-bold">추천 그룹</h1>
      <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
        {/* TODO: 그룹 카드 컴포넌트 */}
        <div className="bg-white p-4 rounded shadow"># 독서토론 클럽</div>
        <div className="bg-white p-4 rounded shadow"># 심리학 책 모임</div>
      </div>

      <h2 className="text-2xl font-bold mt-8">최근 인기 도서</h2>
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        {/* TODO: 도서 카드 컴포넌트 */}
        <div className="bg-white p-4 rounded shadow">『1984』</div>
        <div className="bg-white p-4 rounded shadow">『철학의 위안』</div>
      </div>

      <h2 className="text-2xl font-bold mt-8">최신 글</h2>
      <div className="space-y-3">
        {/* TODO: PostCard 컴포넌트 */}
        <div className="p-3 border rounded">[감상문] 이 책은 나에게 깊은 울림을...</div>
      </div>
    </section>
  )
}
