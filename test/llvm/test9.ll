; ModuleID = '../src/test9.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind
define i32 @test9(i32 %value1) #0 {
  %1 = alloca i32, align 4
  %local1 = alloca i32, align 4
  %n = alloca i32, align 4
  store i32 %value1, i32* %1, align 4
  store i32 0, i32* %n, align 4
  br label %2

; <label>:2                                       ; preds = %8, %0
  %3 = load i32, i32* %n, align 4
  %4 = icmp slt i32 %3, 10
  br i1 %4, label %5, label %11

; <label>:5                                       ; preds = %2
  %6 = load i32, i32* %1, align 4
  %7 = add nsw i32 %6, 10
  store i32 %7, i32* %local1, align 4
  br label %8

; <label>:8                                       ; preds = %5
  %9 = load i32, i32* %n, align 4
  %10 = add nsw i32 %9, 1
  store i32 %10, i32* %n, align 4
  br label %2

; <label>:11                                      ; preds = %2
  %12 = load i32, i32* %local1, align 4
  ret i32 %12
}

attributes #0 = { nounwind "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "target-features"="+mmx,+sse,+sse2" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"clang version 3.8.0-2ubuntu4 (tags/RELEASE_380/final)"}
