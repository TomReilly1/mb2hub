-- AlterTable
ALTER TABLE "kingdoms" ALTER COLUMN "desc_text" DROP NOT NULL;

-- AlterTable
ALTER TABLE "villages" ADD COLUMN     "desc_text" TEXT;
